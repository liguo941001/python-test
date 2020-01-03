from django.urls import path,re_path
from . import views
urlpatterns = [
    path('banners/',views.BannersListAPIView.as_view()),
    path('nav/header/',views.HeaderNavListAPIView.as_view()),
    path('nav/footer/',views.FooterNavAPIView.as_view()),
    path('song-list/',views.SongListAPIView.as_view()),
    path('classify-list/',views.ClassifyListAPIView.as_view()),
    path('up-music/',views.UpMusicListAPIView.as_view()),
    path('new-music/',views.NewMusicListAPIView.as_view()),
    path('original/',views.OriginalMusicListAPIView.as_view()),
]