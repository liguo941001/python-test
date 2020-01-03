from django.core.mail import send_mail
from settings.dev import EMAIL_FROM
import random


def get_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


def send_sms(email, code):
    email_title = '验证码'
    email_body = '您正在登陆拆东墙音乐，此次验证码为 %s ,请务泄露' % code
    email = email
    try:
        send_mail(email_title, email_body, EMAIL_FROM, [email])
    except Exception:
        return False
    return True
