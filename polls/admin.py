from django.contrib import admin

from .models import Question
from .models import Choice
# Question对象具有管理界面
admin.site.register(Question)
admin.site.register(Choice)