from django.contrib import admin

from .models import Question
# Question对象具有管理界面
admin.site.register(Question)