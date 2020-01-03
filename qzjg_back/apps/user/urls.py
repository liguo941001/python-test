from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('email/', views.CheckEmailAPIView.as_view()),
    path('username/', views.CheckUserAPIView.as_view()),
    path('sms/', views.SendSmsAPIView.as_view()),
    path('register/', views.RegisterCreateAPIView.as_view()),
]
