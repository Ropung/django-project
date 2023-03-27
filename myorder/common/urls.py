from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as common_view

urlpatterns = [
    path('', common_view.index, name ='index'),
    path('login', auth_view.LoginView.as_view(template_name = 'common/login.html'),name="login"),
    path('logout', auth_view.LogoutView.as_view(), name ='logout'),
]