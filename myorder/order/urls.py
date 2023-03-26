from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('find_order', views.find_order),
    path('write', views.write),
    path('<int:id>', views.read),
    path('<int:id>/update', views.update),
    path('<int:id>/delete', views.delete),
    path('login', views.login),
    path('logout', views.logout),
]