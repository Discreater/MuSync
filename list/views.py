from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from musync_core.models import User, CurrentList, Track, CurrentListHasTrack
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now, localtime
import datetime
import json


@csrf_exempt
def delete_by_order(request):
    if request.method == 'DELETE':
        user_id = int(request.GET.get('user_id', default=0))
        order = int(request.GET.get('order', default=0))
        if order > 0 and user_id > 0:
            try:
                user = User.objects.get(id=user_id)
                c_clhs = CurrentListHasTrack.objects.get(current_list__user=user, order=order)
                for clhs in CurrentListHasTrack.objects.filter(current_list__user=user, order__gt=order):
                    clhs.order = clhs.order - 1
                    clhs.save()
                c_clhs.delete()
                current_list = CurrentList.objects.get(user=user)
                if current_list.playing_order == order:
                    if not CurrentListHasTrack.objects.filter(current_list=current_list, order=order).exists():
                        current_list.playing_order = 1
                    current_list.begin_time = now()
                    current_list.save()
                return JsonResponse({})
            except ObjectDoesNotExist:
                return JsonResponse({'error': '请求参数非法'}, status=401)
        return JsonResponse({'error': '请求参数非法'}, status=401)
    return JsonResponse({'error': '方法错误'}, status=401)


@csrf_exempt
def pause(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', default=0)
        if user_id != 0:
            try:
                current_list = CurrentList.objects.filter(user__id=user_id)
                if current_list.exists():
                    current_list = CurrentList.objects.get(user__id=user_id)
                    if current_list.is_active == 0:
                        return JsonResponse({})
                    current_list.is_active = 0
                    current_list.pause_time = now()
                    current_list.save()
                return JsonResponse({})
            except ObjectDoesNotExist:
                return JsonResponse(status=401)
    return JsonResponse(status=401)


@csrf_exempt
def play(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', default=0)
        if user_id != 0:
            try:
                current_list = CurrentList.objects.filter(user__id=user_id)
                if current_list.exists():
                    current_list = CurrentList.objects.get(user__id=user_id)
                    if current_list.is_active == 1:
                        return JsonResponse({})
                    current_list.is_active = 1
                    current_list.begin_time = now() - (current_list.pause_time - current_list.begin_time)
                    current_list.save()
                return JsonResponse({})
            except ObjectDoesNotExist:
                return JsonResponse(status=401)
    return JsonResponse(status=401)


@csrf_exempt
def get_current_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', default=0)
        if user_id != 0:
            try:
                user = User.objects.get(id=user_id)
                current_list = CurrentList.objects.filter(user=user)
                if current_list.exists():
                    clht = CurrentListHasTrack.objects.filter(current_list=current_list[0]) \
                        .values('order', 'track_id', 'track__title',
                                'track__artist__name').order_by('order')
                    order = current_list.values()[0]['playing_order']
                    track = clht.get(order=order)['track_id']
                    dic = dict(current_list.values()[0])
                    begin_time = CurrentList.objects.get(user=user).begin_time
                    pause_time = CurrentList.objects.get(user=user).pause_time
                    if begin_time is not None:
                        dic['begin_time'] = begin_time.isoformat()
                    if pause_time is not None:
                        dic['pause_time'] = pause_time.isoformat()
                    dic['track_id'] = track
                    return JsonResponse({'list': list(clht), 'state': dic})
                return JsonResponse({'list': [], 'state': {}})
            except ObjectDoesNotExist:
                return JsonResponse({'list': [], 'state': {}})
        return JsonResponse({'error': '请求参数非法'})
    return JsonResponse({'error': '方法错误'})


@csrf_exempt
def play_now(request):
    if request.method == 'POST':
        # TODO session验证
        try:
            dic = eval(request.body)
            if 'music_id' in dic and 'user_id' in dic and 'short' in dic:
                user = User.objects.get(id=dic['user_id'])
                track = Track.objects.get(id=dic['music_id'])
                is_short = int(dic['short'])
                try:  # 用户存在current_list
                    current_list = CurrentList.objects.get(user=user)
                    if current_list.tracks.count() == 0:  # current_list中无track,
                        current_list_has_track = CurrentListHasTrack(current_list=current_list, track=track,
                                                                     order=1, is_short=is_short)
                        current_list_has_track.save()
                        current_list.is_active = 1
                        current_list.begin_time = now()
                        current_list.playing_order = 1
                        current_list.save()
                    else:  # current_list有track
                        tmp = CurrentListHasTrack.objects.filter(track=track, current_list=current_list)
                        order = current_list.playing_order
                        if not tmp.exists():  # current_list中没有要添加的track
                            for clhs in CurrentListHasTrack.objects.filter(current_list=current_list, order__gt=order):
                                clhs.order = clhs.order + 1
                                clhs.save()
                            CurrentListHasTrack.objects.create(current_list=current_list, track=track, order=order + 1,
                                                               is_short=is_short)
                            # 当前歌单order后移一位并启动
                            if CurrentListHasTrack.objects.filter(current_list=current_list,
                                                                  order=order + 1).exists():
                                current_list.playing_order = order + 1
                            else:
                                current_list.playing_order = 1
                            current_list.begin_time = now()
                            current_list.is_active = 1
                            current_list.save()
                        else:
                            end_order = tmp[0].order
                            print(end_order)
                            if end_order == order:  # 若要播放的就是当前的歌
                                current_list.is_active = 1
                                current_list.begin_time = now()
                                current_list.save()
                            elif end_order > order:  # 若要播放的歌order大于当前的歌
                                for clhs in CurrentListHasTrack.objects.filter(current_list=current_list,
                                                                               order__gt=order,
                                                                               order__lt=end_order):
                                    clhs.order = clhs.order + 1
                                    clhs.save()

                                c_clhs = CurrentListHasTrack.objects.get(current_list=current_list, order=end_order,
                                                                         track=track)
                                c_clhs.order = order + 1
                                c_clhs.save()
                                # 当前歌单order后移一位并启动
                                if CurrentListHasTrack.objects.filter(current_list=current_list,
                                                                      order=order + 1).exists():
                                    current_list.playing_order = order + 1
                                else:
                                    current_list.playing_order = 1
                                current_list.begin_time = now()
                                current_list.is_active = 1
                                current_list.save()
                            elif end_order < order:  # 若要播放的歌order小于当前的歌
                                # 将所有大于要播放的歌，小于等于当前歌的order-1
                                for clhs in CurrentListHasTrack.objects.filter(current_list=current_list,
                                                                               order__lte=order, order__gt=end_order):
                                    clhs.order = clhs.order - 1
                                    clhs.save()
                                # 将要播放的歌设为当前的歌的order，current_list不用改order
                                c_clhs = CurrentListHasTrack.objects.get(current_list=current_list, order=end_order,
                                                                         track=track)
                                c_clhs.order = order
                                c_clhs.save()
                                current_list.begin_time = now()
                                current_list.is_active = 1
                                current_list.save()
                except CurrentList.DoesNotExist:
                    current_list = CurrentList(user=user, begin_time=now(), is_active=1, playing_order=1)
                    current_list.save()
                    current_list_has_track = CurrentListHasTrack(current_list=current_list, track=track, order=1,
                                                                 is_short=is_short)
                    current_list_has_track.save()
                current_list = CurrentList.objects.get(user=user)
                r_list = CurrentListHasTrack.objects.filter(current_list=current_list).values()
                dic = CurrentList.objects.filter(user=user).values()[0]
                return JsonResponse({'list': list(r_list), 'state': dic})
            else:
                return JsonResponse({'error': '请求参数非法'}, status=401)
        except ObjectDoesNotExist:
            return JsonResponse({'error': '请求参数非法'}, status=401)
    return JsonResponse({'error': '方法错误'}, status=401)


@csrf_exempt
def add_to_next_play(request):
    if request.method == 'POST':
        # TODO session验证
        try:
            dic = eval(request.body)
            if 'music_id' in dic and 'user_id' in dic and 'short' in dic:
                user = User.objects.get(id=dic['user_id'])
                track = Track.objects.get(id=dic['music_id'])
                is_short = int(dic['short'])
                try:  # 用户存在current_list
                    current_list = CurrentList.objects.get(user=user)
                    if current_list.tracks.count() == 0:  # current_list中无track,
                        current_list_has_track = CurrentListHasTrack(current_list=current_list, track=track,
                                                                     order=1, is_short=is_short)
                        current_list_has_track.save()
                        current_list.is_active = 1
                        current_list.begin_time = now()
                        current_list.playing_order = 1
                        current_list.save()
                    else:  # current_list有track
                        tmp = CurrentListHasTrack.objects.filter(track=track, current_list=current_list)
                        order = current_list.playing_order
                        if not tmp.exists():
                            for clhs in CurrentListHasTrack.objects.filter(current_list=current_list, order__gt=order):
                                clhs.order = clhs.order + 1
                                clhs.save()
                            CurrentListHasTrack.objects.create(current_list=current_list, track=track, order=order + 1,
                                                               is_short=is_short)

                        else:
                            end_order = tmp[0].order
                            print(end_order)
                            if end_order == order:  # 若要添加的就是当前的歌， 重新播放
                                current_list.is_active = 1
                                current_list.begin_time = now()
                                current_list.save()
                            elif end_order > order:  # 若要添加的歌order大于当前的歌
                                for clhs in CurrentListHasTrack.objects.filter(current_list=current_list,
                                                                               order__gt=order,
                                                                               order__lt=end_order):
                                    clhs.order = clhs.order + 1
                                    clhs.save()

                                c_clhs = CurrentListHasTrack.objects.get(current_list=current_list, order=end_order,
                                                                         track=track)
                                c_clhs.order = order + 1
                                c_clhs.save()
                            elif end_order < order:  # 若要添加的歌order小于当前的歌
                                # 将所有大于要播放的歌、小于等于当前歌的order-1
                                for clhs in CurrentListHasTrack.objects.filter(current_list=current_list,
                                                                               order__lte=order, order__gt=end_order):
                                    clhs.order = clhs.order - 1
                                    clhs.save()
                                # 将要添加的歌设为当前的歌的order，current_list的order随当前歌的order-1
                                c_clhs = CurrentListHasTrack.objects.get(current_list=current_list, order=end_order,
                                                                         track=track)
                                c_clhs.order = order
                                c_clhs.save()
                                current_list.playing_order = current_list.playing_order - 1
                                current_list.begin_time = now()
                                current_list.is_active = 1
                                current_list.save()
                except CurrentList.DoesNotExist:
                    current_list = CurrentList(user=user, begin_time=now(), is_active=1, playing_order=1)
                    current_list.save()
                    current_list_has_track = CurrentListHasTrack(current_list=current_list, track=track, order=1,
                                                                 is_short=is_short)
                    current_list_has_track.save()
                current_list = CurrentList.objects.get(user=user)
                r_list = CurrentListHasTrack.objects.filter(current_list=current_list).values()
                dic = CurrentList.objects.filter(user=user).values()[0]
                return JsonResponse({'list': list(r_list), 'state': dic})
            else:
                return JsonResponse({'error': '请求参数非法'}, status=401)
        except ObjectDoesNotExist:
            return JsonResponse({'error': '请求参数非法'}, status=401)
    elif request.method == 'GET':
        user_id = request.GET.get('user_id', default=0)
        if user_id == 0:
            return JsonResponse({'error': '请求参数非法'}, status=401)
        current_list = CurrentList.objects.get(user_id=user_id)
        if CurrentListHasTrack.objects.filter(current_list=current_list, order=current_list.playing_order + 1).exists():
            current_list.playing_order = current_list.playing_order + 1
        else:
            current_list.playing_order = 1
        current_list.begin_time = now()
        current_list.is_active = 1
        current_list.save()
        r_list = CurrentListHasTrack.objects.filter(current_list=current_list).values()
        dic = CurrentList.objects.filter(user_id=user_id).values()[0]
        return JsonResponse({'list': list(r_list), 'state': dic})


def get_current_track(current_list):
    c_track = CurrentListHasTrack.objects.filter(current_list=current_list, is_playing=1)
    if c_track.exists():
        track = c_track[0].track
        while True:
            if c_track[0].is_short == 1:
                duration = track.short_duration
            else:
                duration = track.duration
            if c_track[0].play_time + datetime.timedelta(seconds=duration) > now():
                return track
            c_track = CurrentListHasTrack.objects.filter(current_list=current_list, order=c_track[0].order + 1)
            if not c_track.exists():
                c_track = CurrentListHasTrack.objects.filter(current_list=current_list, order=1)
            track = c_track[0].track
