from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name ='index'),
    path('write', views.write, name= 'write'),
    path('<int:id>', views.read, name ='detail'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name ='delete'),
]