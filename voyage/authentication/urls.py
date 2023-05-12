
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import CustomUserView
from django.urls import path
from .views import RegistrationView, ObtainTokenPairView


urlpatterns = [
 path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
 path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
 path('register/', RegistrationView.as_view(), name='register'),
 path('users/', CustomUserView.as_view(), name='users'),

]


