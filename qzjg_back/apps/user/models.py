from django.db import models
from django.contrib.auth.models import AbstractUser
from qzjg_back.utils import model


#
#
class User(AbstractUser):
    email = models.CharField(max_length=32, verbose_name='邮箱', unique=True)

    class Meta:
        db_table = 'qzjg_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 用户信息表
class UserInfo(model.BaseModel):
    user = models.OneToOneField(to='User', on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to='avatar', verbose_name='用户头像', null=True, blank=True,
                               help_text='头像图片大小规格: 256x256,或者对应比例的图片', default='media/avatar/default.jpg')
    signature = models.CharField(max_length=64, null=True, verbose_name='个性签名', blank=True)

    class Meta:
        db_table = 'user_info'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


# 歌手表
class Singer(model.BaseModel):
    name = models.CharField(max_length=32, verbose_name='歌手名称')
    note = models.CharField(max_length=128, verbose_name='歌手简介')
    avatar = models.ImageField(upload_to='picture', verbose_name='歌手头像', null=True, blank=True,
                               default='media/picture/default.jpg')
    enshrine_num = models.IntegerField(verbose_name='收藏数量', default=0, null=True)


    class Meta:
        db_table = 'qzjg_singer'
        verbose_name = '歌手信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 歌曲作者表
class Author(model.BaseModel):
    name = models.CharField(max_length=32, verbose_name='作者')

    class Meta:
        db_table = 'qzjg_author'
        verbose_name = '作者表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

