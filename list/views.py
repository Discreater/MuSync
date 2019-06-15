from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from musync_core.models import User, CurrentList, Track, CurrentListHasTrack
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now, localtime
import json


# Create your views here.
@csrf_exempt
def add_to_next_play(request):
    if request.method == 'POST':
        # TODO session验证
        try:
            dic = eval(request.body)
            if 'music_id' in dic and 'user_id' in dic and 'is_short' in dic:
                user = User.objects.get(id=dic['user_id'])
                track = Track.objects.get(id=dic['music_id'])
                is_short = int(dic['is_short'])
                try:
                    current_list = CurrentList.objects.get(user=user)
                    if current_list.tracks.count() == 0:
                        current_list_has_track = CurrentListHasTrack(current_list=current_list, track=track,
                                                                     is_playing=1, order=1, play_time=now(), is_short=is_short)
                        current_list_has_track.save()
                    else:
                        playing_track = CurrentList.objects.filter()
                        for clhs in CurrentListHasTrack.objects.filter(current_list=current_list, order__gt=1):
                            clhs.order = clhs.order + 1
                            clhs.save()
                        CurrentListHasTrack.objects.create(current_list=current_list, track=track, order=2, is_short=is_short)
                except CurrentList.DoesNotExist:
                    current_list = CurrentList(user=user)
                    current_list.save()
                    current_list_has_track = CurrentListHasTrack(current_list=current_list, track=track, is_playing=1, order=1, play_time=now(), is_short=is_short)
                    current_list_has_track.save()
                

            else:
                return JsonResponse({'error': '请求参数非法'}, status=401)


        except ObjectDoesNotExist:
            return JsonResponse({'error': '请求参数非法'}, status=401)
