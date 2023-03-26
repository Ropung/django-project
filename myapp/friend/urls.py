from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_friend/', views.add_friend),
    path('create_friend/', views.create_friend),
    path('show_all/', views.show_all),
    path('find_friend/', views.find_friend),
    path('delete_friend/<int:id>/', views.delete_friend),
    path('update_friend/<int:id>/', views.update_friend),
    # path('list', views.index),
]