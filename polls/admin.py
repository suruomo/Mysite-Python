from django.contrib import admin
from .models import Question
from .models import Choice

# 自定义后台管理样式
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 页面显示
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 字段分集管理
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
# Question,Choice对象具有管理界面
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)