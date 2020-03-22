from django.db import models
import datetime
from django.utils import timezone
# 创建数据库模型
class Question(models.Model):
    # 问题
    question_text = models.CharField(max_length=200)
    # 出版日期
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # 问题：与Question外键关联
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 选择文本
    choice_text = models.CharField(max_length=200)
    # 投票提示
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)