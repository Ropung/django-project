from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.read),
    path('write', views.write),
    path('<int:id>/update', views.update),
    path('<int:id>/delete', views.delete),
]