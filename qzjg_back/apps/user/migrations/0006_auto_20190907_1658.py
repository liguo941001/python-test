# Generated by Django 2.1.8 on 2019-09-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190907_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song_list',
            name='note',
            field=models.CharField(max_length=256, verbose_name='歌单简介'),
        ),
    ]
