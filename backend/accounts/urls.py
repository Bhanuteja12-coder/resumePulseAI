from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import CustomTokenObtainPairView, RegisterAPIView, UserMeAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("register", RegisterAPIView.as_view()),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login", CustomTokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("refresh", TokenRefreshView.as_view()),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("verify", TokenVerifyView.as_view()),
    path("me/", UserMeAPIView.as_view(), name="user_me"),
    path("me", UserMeAPIView.as_view()),
]
