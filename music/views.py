from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from musync_core.models import Track
import json
from django.core.exceptions import ObjectDoesNotExist
import re


@csrf_exempt
def search(request):
    if request.method == 'GET':
        q = request.GET.get('q', default='')
        p = int(request.GET.get('p', default='1'))
        ps = int(request.GET.get('ps', default='7'))
        if p < 1:
            p = 1
        if ps < 1:
            ps = 7
        ans_set = Track.objects.filter(title__icontains=q, is_short_cached=1).distinct() \
            .values('id', 'title', 'duration', 'is_short_cached', 'yun_id', 'has_lyric', 'artist_id',
                        'artist__name', 'album_id', 'album__title', 'information', 'tags', 'is_cached', 'short_duration')
        # 仅搜索歌曲名， 注释掉的是搜索专辑名
        # ans_set = (ans_set | Track.objects.filter(album__title__icontains=qi).distinct()).distinct()
        ans_list = list(ans_set[(p - 1) * ps: p * ps])
        for order, ans in enumerate(ans_list):
            ans['order'] = order + 1 + (p - 1) * ps
        return JsonResponse({'musics': ans_list, 'count': ans_set.count()})
    else:
        return JsonResponse({'error', '方法错误'}, status=401)
