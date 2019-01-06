from django.http import JsonResponse
from rest_framework.views import APIView
from account.models import Users, Tokens
import json
import hashlib
from datetime import datetime, timedelta
from account.serializers import UsersSerializer


def md5(user):
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


# Create your views here.
class AuthView(APIView):

    def post(self, request, *args, **kwargs):

        ret = {'code': 0, 'msg': 'success'}
        try:
            if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
            body = json.loads(request.body)
            login_type = body.get('login_type')
            login_name = body.get('login_name')
            password = body.get('password')
            if login_type == 1:
                if not Users.objects.filter(mobile=login_name).first():     # 用户不存在
                    # create a new user，return token and update "token" table
                    u1 = Users.objects.create(login_type=login_type, mobile=login_name, password=password,
                                              last_login_ip=ip, create_date=datetime.now(),
                                              last_login_date=datetime.now())
                    u1.password = hashlib.sha1(bytes(password+u1.user_id.__str__(), encoding='utf-8')).hexdigest()
                    u1.save(update_fields=['password'])
                    token = md5(login_name)
                    Tokens.objects.create(user=u1,
                                          token=token,
                                          expire_to=datetime.now()+timedelta(hours=3))
                    ret['token'] = token
                    return JsonResponse(ret)
                else:   # 用户存在
                    u1 = Users.objects.filter(mobile=login_name).first()
                    encrypt = hashlib.sha1(bytes(password+u1.user_id.__str__(), encoding='utf-8')).hexdigest()
                    if encrypt == u1.password:  # 密码匹配
                        u1.last_login_date = datetime.now()
                        u1.last_login_ip = ip
                        u1.save(update_fields=['last_login_date', 'last_login_date'])
                        ret['token'] = Tokens.objects.filter(user=u1).first().token
                        return JsonResponse(ret)
                    else:   # 密码错误
                        ret = {'code': 101, 'msg': 'incorrect password'}
                        return JsonResponse(ret)
            elif login_type == 2:
                pass
            elif login_type == 3:
                pass
            else:
                ret = {'code': 100, 'msg': 'incorrect login type'}
                return JsonResponse(ret)
        except Exception as e:
            print(e)
        finally:
            return JsonResponse(ret)
