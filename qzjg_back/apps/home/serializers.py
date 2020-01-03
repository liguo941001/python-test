from rest_framework import serializers

from . import models


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ('image', 'link')


class NavModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nav
        fields = ('name', 'link')


class SongListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song_List
        fields = ('name', 'note', 'cover', 'play_num')


class ClassModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classify
        fields = ('name', 'pk')


class UpMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = ('name', 'pk', 'enshrine_num')


class NewMusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = ('name', 'pk', 'enshrine_num')


class OriginalMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = ('name', 'pk', 'enshrine_num')
