from django.conf.urls import url
from . import views

urlpatterns = [
    url('register', views.user_register, name='register'),
    url('login', views.login_view, name='login'),
    url('logout', views.logout_view, name='logout')
]