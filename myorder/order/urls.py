from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('write', views.write, name= 'write'),
    path('<int:id>', views.read, name ='detail'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name ='delete'),
    # path('login', views.login, name ='login'),
    # path('logout', views.logout, name ='logout'),
    # path('signup', views.signup, name ='signup'),
]