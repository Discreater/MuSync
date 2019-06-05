from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from musync_core.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def registerApi(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        user_id = req['userID']
        pwd = req['pwd']
        try:
            search_array = User.objects.get(id=user_id)
            print(search_array)
            return JsonResponse({'result': 200, 'msg': '已有重复用户名'})
        except ObjectDoesNotExist:
            return JsonResponse({'result': 200, 'msg': '注册成功'})


def hello(request):
    return JsonResponse({'result': 200, 'msg': 'hello, 连接成功'})


def registerPage(request):
    return render_to_response("register/register.html")
