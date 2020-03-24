from django.http import HttpResponse
from django.template import loader
from .models import Question
# 视图
# 问题索引页
def index(request):
    # 按日期查找最新5条记录
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 加载视图模板
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # render()载入模板，填充上下文，再返回由它生成的HttpResponse对象
    return HttpResponse(template.render(context, request))
# 投票详情页
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
# 投票结果
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
# 投票处理
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)