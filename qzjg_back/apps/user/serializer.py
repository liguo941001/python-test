from rest_framework import serializers
from . import models
from django.core.cache import cache
import re

class RegisterModelSerializer(serializers.ModelSerializer):
    # 只参与反序列话的插拔式字段
    sms = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = models.User
        fields = ('username','email', 'password', 'sms')
        extra_kwargs = {
            'sms': {
                'error_messages': {
                    'required': '验证码不能为空'
                }
            },
            'password':{
                'write_only':True
            },
        }

    def validate_email(self, value):
        if not re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', value):
            raise serializers.ValidationError('该邮箱不合法')
        if models.User.objects.filter(email=value):
            raise serializers.ValidationError('该邮箱已存在')
        return value


    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('密码不合法')
        return value

    def validate(self, attrs):
        print(attrs)
        email = attrs.get('email')
        code = attrs.pop('sms')
        if code != cache.get('sms_%s' % email):
            raise serializers.ValidationError({'sms':'验证码有误'})
        return attrs
    def create(self,validated_data):
        print(validated_data)
        return models.User.objects.create_user(**validated_data)
