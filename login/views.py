from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from musync_core.models import User
import json
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def change_info(request):
    if request.method == 'POST':
        try:
            # TODO 验证request.body
            user = User.objects.get(id=request.POST.get('id', 0))
            user.name = request.POST.get('name', 0)
            user.email = request.POST.get('email', '')
            user.gender = request.POST.get('gender', '')
            user.phone = request.POST.get('phone', '')
            user.save()
            return JsonResponse({})
        except ObjectDoesNotExist:
            return JsonResponse({'error': '请求参数非法'}, status=401)
    return JsonResponse({'error': '方法错误'}, status=401)


@csrf_exempt
def fetch_info(request, user_id):
    if request.method == 'GET':
        if user_id > 0:
            try:
                user = User.objects.get(id=user_id)
                dic = user.__dict__
                dic.pop('_state')
                birth_date = dic['birth_date']
                if birth_date is not None:
                    dic['birth_date'] = birth_date.isoformat()
                return JsonResponse({'info': dic})
            except ObjectDoesNotExist:
                return JsonResponse({'error': '请求参数非法1'}, status=401)
        return JsonResponse({'error': '请求参数非法'}, status=401)
    return JsonResponse({'error': '方法错误'}, status=401)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            dic = eval(request.body)
            if 'name' in dic and 'password' in dic:
                user = User.objects.get(name=dic['name'])
                if user.password == dic['password']:
                    resp = {'status': 'success', 'user_id': user.id}
                    request.session['user_id'] = user.id
                    return HttpResponse(json.dumps(resp), content_type="application/json")
                else:
                    resp = {'error': 'password'}
                    return HttpResponse(json.dumps(resp), content_type="application/json", status=401)
            else:
                resp = {'error': 'parameter'}
                return HttpResponse(json.dumps(resp), content_type="application/json", status=401)
        except ObjectDoesNotExist:
            resp = {'error': 'name'}
            return HttpResponse(json.dumps(resp), content_type="application/json", status=401)
    else:
        resp = {'error': 'method'}
        return HttpResponse(json.dumps(resp), content_type="application/json", status=401)


@csrf_exempt
def logout(request):
    if request.method == 'DELETE':
        if 'user_id' in request.session:
            # 删除整个会话
            request.session.flush()
    return HttpResponse()
