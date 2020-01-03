from . import models
from . import serializer
from utils.APIResponse import APIResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib import auth
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler
from utils.SMS import send_sms, get_code
from django.core.cache import cache
from settings.dev import EX_TIME
import re


# 注册接口
class RegisterCreateAPIView(CreateAPIView):
    queryset = models.User.objects
    serializer_class = serializer.RegisterModelSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return APIResponse(0, 'ok', user=response.data)

# 校验邮箱基类
class CheckEmailBaseAPIView(APIView):
    def check_email(self, email):
        if not email:
            return APIResponse(1, '邮箱不能为空')
        if not re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', email):
            return APIResponse(1, '邮箱格式不正确')
        return None


# 查看用户名接口
class CheckUserAPIView(APIView):
    def get(self, request):
        request_date = request.query_params
        username = request_date.get('username')
        if not username:
            return APIResponse(1, '用户名不能为空')
        if not re.match(r'^[a-zA-Z0-9_-]{4,16}$', username):
            return APIResponse(1, '用户名不合法')
        if models.User.objects.filter(username=username):
            return APIResponse(1, '用户名已存在')
        else:
            return APIResponse(0, '用户名可使用')


# 查看邮箱接口
class CheckEmailAPIView(CheckEmailBaseAPIView):
    def get(self, request):
        request_data = request.query_params
        email = request_data.get('email')
        response = self.check_email(email)
        if not response:
            user_obj = models.User.objects.filter(email=email)
            if user_obj:
                return APIResponse(1, '邮箱已存在')
            return APIResponse(0, '该邮箱可以使用')
        else:
            return response


# 邮箱验证码
class SendSmsAPIView(CheckEmailBaseAPIView):
    def get(self, request):
        request_data = request.query_params
        email = request_data.get('email')
        response = self.check_email(email)
        if response:
            return response
        code = get_code()
        print(code)
        # 发送验证码
        result = send_sms(email, code)
        if not result:
            return APIResponse(1, '验证码发送失败')
        # 验证码存储到内存，redis
        cache.set('sms_%s' % email, code, EX_TIME)
        return APIResponse(0, '验证码发送成功')


# 多方式登陆接口
class LoginAPIView(APIView):
    def post(self, request):
        request_data = request.data
        username = request_data.get('username')
        password = request_data.get('password')
        email = request_data.get('email')
        if username:
            user_obj = auth.authenticate(username=username, password=password)
            if not (user_obj and user_obj.is_active):
                user_obj = None
        else:
            user_obj = models.User.objects.filter(email=email).first()
            print(user_obj)
            if not user_obj.check_password(password):
                user_obj = None
        if user_obj:
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            return APIResponse(0, 'ok', results={
                'username': user_obj.username,
                'token': token
            })
        else:
            return APIResponse(1, '用户名或密码错误')
