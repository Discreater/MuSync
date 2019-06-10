from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from musync_core.models import User
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            dic = eval(request.body)
            if 'name' in dic and 'password' in dic:
                user = User.objects.get(name=dic['name'])
                if user.password == dic['password']:
                    print(request.session.session_key)
                    resp = {'status': 'success', 'user_id': user.id}
                    request.session['user_id'] = user.id
                    return HttpResponse(json.dumps(resp), content_type="application/json")
                else:
                    resp = {'error': 'password'}
                    return HttpResponse(json.dumps(resp), content_type="application/json", status=401)
            else:
                resp = {'error': 'parameter'}
                return HttpResponse(json.dumps(resp), content_type="application/json", status=401)
        except:
            resp = {'error': 'name'}
            return HttpResponse(json.dumps(resp), content_type="application/json", status=401)
    else:
        resp = {'error': 'method'}
        return HttpResponse(json.dumps(resp), content_type="application/json", status=401)
