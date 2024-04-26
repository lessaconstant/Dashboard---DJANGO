from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import register, login_user, register_success, logout_user


urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login'),
    path('register/success/', register_success, name='register_success' ),
    path('logout/', logout_user, name='logout')
]