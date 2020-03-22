from django.urls import path

from . import views
# 视图映射
urlpatterns = [
    path('', views.index, name='index'),
]