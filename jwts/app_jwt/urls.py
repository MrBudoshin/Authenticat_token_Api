from django.urls import path

from .views import UserAPIView, NewsAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
    path('posts/', NewsAPIView.as_view(), name='user'),
]