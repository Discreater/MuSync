from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from musync_core.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json


@csrf_exempt
def get_friends(request, user_id):
    if request.method == 'GET':
        # TODO session验证
        try:
            user = User.objects.get(id=user_id)
            friends = user.friends.all().values('id', 'name', 'signature', 'is_online', 'is_stealth')
            return JsonResponse({'friends': list(friends)})
        except ObjectDoesNotExist:
            return JsonResponse({'error': '用户不存在'}, status=401)
    else:
        return JsonResponse({'error': '方法错误'}, status=401)
