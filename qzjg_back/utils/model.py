from django.db import models


class BaseModel(models.Model):
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True, blank=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True, blank=True)

    class Meta:
        # 设置抽象模型，经行数据库迁移的时候不会为这个模型单独创建一个数据
        abstract = True
