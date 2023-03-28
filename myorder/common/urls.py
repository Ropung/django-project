from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as common_view


app_name = 'common'

urlpatterns = [
    # common 
    
    path('', common_view.index, name ='index'),
    # path('signup', common_view.signup , name ='signup'),
    path('signup', common_view.signup_custom , name ='signup'),
    path('update', common_view.update , name ='update'),
    path('delete', common_view.delete , name ='delete'),
    
    # 회원관련
    path('login', auth_view.LoginView.as_view(template_name = 'common/login.html'),name="login"),
    path('logout', auth_view.LogoutView.as_view(), name ='logout'),
]
