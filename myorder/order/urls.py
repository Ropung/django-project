from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name ='index'),
    # about order 관련
    path('write', views.write, name= 'write'),
    path('<int:id>', views.read, name ='detail'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name ='delete'),

    # about reply
    path('<int:id>/write_reply', views.write_reply, name ='write_reply'),
    path('<int:id>/delete_reply', views.delete_reply, name ='delete_reply'),
    path('<int:id>/update_reply', views.update_reply, name ='update_reply'),

    # about Ajax
    path('call_ajax', views.call_ajax, name ='call_ajax'),
    path('<int:id>/load_reply', views.load_reply, name ='load_reply'),
    path('<int:id>/download', views.download, name ='download'),

    #CBV 방식으로 호출할 주소
    # as_view() 클래스를 뷰의 기능으로서 사용하겠다.
    path('cbv', views.OrderList.as_view(), name = 'cbv'),
    path('cbv/<int:id>', views.OrderDetail.as_view(), name = 'cbv_detail')
]