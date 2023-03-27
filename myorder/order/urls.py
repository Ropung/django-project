from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('write', views.write),
    path('<int:id>', views.read),
    path('<int:id>/update', views.update),
    path('<int:id>/delete', views.delete),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),
]