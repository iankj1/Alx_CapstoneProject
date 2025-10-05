from django.urls import path
from users.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('api/users/login/', TokenObtainPairView.as_view(), name='login'),
]
