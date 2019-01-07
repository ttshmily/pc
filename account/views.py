from django.http import JsonResponse
from rest_framework.views import APIView
from account.models import Users, Tokens
import json
import hashlib
import re
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

    def post(self, request):
        """
        登录或注册接口。
        如果用户名存在，则验证密码，密码正确返回token，密码错误返回错误
        如果用户名不存在，则创建新用户，返回token。
        :param request:
        :return: token
        """
        ret = {'code': 0, 'msg': 'success'}
        try:
            if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
            body = json.loads(request.body)
            login_name = body.get('login_name')
            password = body.get('password')

            if not Users.objects.get(mobile=login_name):     # 用户不存在
                # create a new user，return token and update "token" table
                if not re.match(r'(.*)@', login_name):
                    u1 = Users.objects.create(signup_type=1, mobile=login_name, password=password,
                                              last_login_ip=ip, create_date=datetime.now(),
                                              last_login_date=datetime.now())
                else:
                    u1 = Users.objects.create(signup_type=2, email=login_name, password=password,
                                              last_login_ip=ip, create_date=datetime.now(),
                                              last_login_date=datetime.now())
                u1.password = hashlib.sha1(bytes(password+u1.user_id.__str__(), encoding='utf-8')).hexdigest()
                u1.save(update_fields=['password'])
                token = md5(u1.user_id)
                Tokens.objects.create(user=u1,
                                      token=token,
                                      expire_to=datetime.now()+timedelta(minutes=3))
                ret['token'] = token
                # return JsonResponse(ret)
            else:   # 用户存在
                if not re.match(r'(.*)@', login_name):
                    u1 = Users.objects.get(mobile=login_name)
                else:
                    u1 = Users.objects.get(email=login_name)
                encrypt = hashlib.sha1(bytes(password+u1.user_id.__str__(), encoding='utf-8')).hexdigest()
                if encrypt == u1.password:  # 密码匹配
                    u1.last_login_date = datetime.now()
                    u1.last_login_ip = ip
                    u1.save(update_fields=['last_login_date', 'last_login_date'])
                    t1 = Tokens.objects.filter(user=u1).order_by("-id").first()
                    if t1.token and datetime.now()+timedelta(minutes=1) < t1.expire_to:
                        ret['token'] = t1.token
                    else:
                        token = md5(u1.user_id)
                        Tokens.objects.create(user=u1,
                                              token=token,
                                              expire_to=datetime.now() + timedelta(minutes=3))
                        ret['token'] = token
                    # return JsonResponse(ret)
                else:   # 密码错误
                    ret = {'code': 101, 'msg': 'incorrect password'}
                    # return JsonResponse(ret)
        except Exception as e:
            print("exceptions CAUGHT!!!" + e)
            ret = {'code': 1000, 'msg': 'unknown error'}
        finally:
            return JsonResponse(ret)
