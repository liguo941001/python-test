from django.db import models
from qzjg_back.utils import model
from user.models import User, Author, Singer


# Create your models here.
class Banner(model.BaseModel):
    '''轮播图'''
    # upload_to 存储子目录，真实存放地址会使用配置中的MADIE_ROOT+upload_to
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True, blank=True)
    name = models.CharField(max_length=150, verbose_name='轮播图名称')
    note = models.CharField(max_length=150, verbose_name='轮播图信息')
    link = models.CharField(max_length=150, verbose_name='轮播图广告地址')

    class Meta:
        db_table = 'qzjg_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Nav(model.BaseModel):
    NAV_POSITION = (
        (0, '顶部导航'),
        (1, '底部导肮')
    )
    name = models.CharField(max_length=32, verbose_name='导航名称')
    link = models.CharField(max_length=64, verbose_name='导航地址')
    opt = models.SmallIntegerField(choices=NAV_POSITION, default=0, verbose_name='位置')

    class Meta:
        db_table = 'qzjg_nav'
        verbose_name = '导航'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 分类
class Classify(model.BaseModel):
    name = models.CharField(max_length=32)
    Song_List = models.ManyToManyField(to='Song_List', related_name='Song_List', db_constraint=False, verbose_name='歌单',
                                       blank=True)

    class Meta:
        db_table = 'qzjg_classify'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 歌单表
class Song_List(model.BaseModel):
    name = models.CharField(max_length=32, verbose_name='歌单名称')
    note = models.CharField(max_length=256, verbose_name='歌单简介')
    cover = models.ImageField(upload_to='cover', verbose_name='封面图', null=True, blank=True)
    play_num = models.IntegerField(verbose_name='播放数量', default=0, null=True, )
    user_music_list = models.ManyToManyField(to=User, related_name='music_list', db_constraint=False,
                                             verbose_name='用户歌单', blank=True)

    class Meta:
        db_table = 'song_list'
        verbose_name = '歌单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 歌曲表
class Music(model.BaseModel):
    name = models.CharField(max_length=32, verbose_name='歌曲名')
    music = models.FileField(upload_to='music', verbose_name='歌曲', null=True, blank=True)
    singer = models.ForeignKey(to=Singer, null=True, on_delete=models.DO_NOTHING, verbose_name='演唱者')
    user = models.ManyToManyField(to=User, related_name='user', db_constraint=False,
                                  verbose_name='用户歌曲', blank=True)
    enshrine_num = models.IntegerField(verbose_name='收藏数量', default=0, null=True)
    author = models.ForeignKey(to=Author, null=True, on_delete=models.DO_NOTHING, verbose_name='作者')
    song_list = models.ManyToManyField(to='Song_List', related_name='song_list', db_constraint=False, verbose_name='歌单',
                                       blank=True)

    class Meta:
        db_table = 'qzjg_Music'
        verbose_name = '歌曲表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name