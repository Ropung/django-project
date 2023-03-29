from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name ='index'),
    # order 관련
    path('write', views.write, name= 'write'),
    path('<int:id>', views.read, name ='detail'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name ='delete'),

    # reply 관련
    path('<int:id>/write_reply', views.write_reply, name ='write_reply'),
    path('<int:id>/delete_reply/<int:rid>', views.delete_reply, name ='delete_reply'),
    path('<int:id>/update_reply', views.update_reply, name ='update_reply'),

]