from rest_framework import filters
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated

from .serializer import UserSerializer, PostSerializer, TokenObtainPairResponseSerializer, \
    TokenVerifyResponseSerializer, TokenRefreshResponseSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .models import News


class NewsAPIView(ListModelMixin, CreateModelMixin, TokenObtainPairView, GenericAPIView):
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['news__title']

    @swagger_auto_schema(responses={status.HTTP_200_OK: PostSerializer})
    def get(self, request):
        return self.list(request)

    @swagger_auto_schema(responses={status.HTTP_200_OK: PostSerializer})
    def post(self, request):
        return self.create(request)


class UserAPIView(RetrieveAPIView, TokenObtainPairView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: UserSerializer})
    def get_object(self):
        return self.request.user


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(responses={status.HTTP_200_OK: TokenRefreshResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: TokenVerifyResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)