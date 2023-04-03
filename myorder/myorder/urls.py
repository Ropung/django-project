
from django.contrib import admin
from django.urls import path,include
# 현재 프로젝트의 settrings.py
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('', include('common.urls')),
    path('order/', include('order.urls')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
