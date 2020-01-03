import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qzjg_back.settings.dev')
django.setup()
from django.conf import settings
from settings.dev import EMAIL_FROM



# from django.core.mail import send_mail
# email_title = '验证码'
# email_body = '您正在登陆拆东墙音乐，此次验证码为：1234 ,请务泄露'
# email = '1207328993@qq.com'
# send_mail(email_title,email_body,EMAIL_FROM,[email])