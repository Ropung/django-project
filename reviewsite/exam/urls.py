from django.urls import path

from . import views

app_name = 'exam'

urlpatterns = [
    path('', views.index, name ='index'),
    path('write', views.write, name= 'write'),
    path('<int:id>', views.read, name ='read'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name ='delete'),
    path('<int:id>/write_review', views.write_review, name ='write_review'),
]