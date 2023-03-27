
from django.contrib import admin
from django.urls import path,include
# from order.views import home

urlpatterns = [
    path('', include('common.urls')),
    path('order/', include('order.urls')),
    path("admin/", admin.site.urls),
]
