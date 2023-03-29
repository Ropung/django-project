from django.contrib import admin
from .models import Order,Reply
# Register your models here.
# 내가 만든 커스텀 모델 등록
admin.site.register(Order)
admin.site.register(Reply)