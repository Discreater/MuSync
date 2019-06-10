from django.shortcuts import render, render_to_response
from django.http import JsonResponse, HttpResponse
from musync_core.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            req = eval(request.body)
            if 'name' in req and 'password' in req and 'email' in req:
                if len(req['name']) < 3 or len(req['name']) >= 255:
                    return JsonResponse({'error': 'name'}, status=401)
                if len(req['password']) < 6 or len(req['password']) >= 45:
                    return JsonResponse({'error': 'name'}, status=401)
                q_user = User.objects.filter(name=req['name'])
                if q_user.count() == 0:
                    n_user = User(name=req['name'], password=req['password'], email=req['email'])
                    n_user.save()
                    return JsonResponse({'status': 'success', 'user_id': n_user.id})
                else:
                    return JsonResponse({'error': 'name_dupli'}, status=401)
            else:
                return JsonResponse({'error': 'name'}, status=401)
        except:
            res = {'error': 'parameter'}
            return JsonResponse(res, status=401)
    else:
        res = {'error': 'method'}
        return JsonResponse(res, status=401)


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
