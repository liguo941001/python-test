from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from . import models, serializers
from utils.APIResponse import APIResponse


# Create your views here.

class BannersListAPIView(ListAPIView):
    queryset = models.Banner.objects.filter(is_delete=False).order_by('-create_time')[:4]
    serializer_class = serializers.BannerModelSerializer


class HeaderNavListAPIView(ListAPIView):
    queryset = models.Nav.objects.filter(is_delete=False, opt=0)
    serializer_class = serializers.NavModelSerializer


class FooterNavAPIView(ListAPIView):
    queryset = models.Nav.objects.filter(is_delete=False, opt=1)
    serializer_class = serializers.NavModelSerializer


class SongListAPIView(ListAPIView):
    queryset = models.Song_List.objects.filter().order_by('-play_num')[:8]
    serializer_class = serializers.SongListModelSerializer


class ClassifyListAPIView(ListAPIView):
    queryset = models.Classify.objects.filter(is_delete=False)
    serializer_class = serializers.ClassModelSerializer


class UpMusicListAPIView(ListAPIView):
    queryset = models.Music.objects.filter(is_delete=False).order_by('-create_time').order_by('-enshrine_num')[:10]
    serializer_class = serializers.UpMusicListSerializer


class NewMusicListAPIView(ListAPIView):
    queryset = models.Music.objects.filter(is_delete=False).order_by('-create_time')[:10]
    serializer_class = serializers.NewMusicListSerializer


class OriginalMusicListAPIView(ListAPIView):
    queryset = models.Music.objects.filter(is_delete=False,author__name=F('singer__name'))
    serializer_class = serializers.OriginalMusicSerializer

