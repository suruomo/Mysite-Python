from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from .models import Question,Choice
from django.urls import reverse
from django.views import generic

# 问题索引视图
# ListView通用视图显示一个对象列表
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# 问题详情视图
# DetailView视图显示一个对象的详细信息界面
class DetailView(generic.DetailView):
    # 视图作用模型，由model提供
    model = Question
    template_name = 'polls/detail.html'

# 投票结果视图
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# 投票处理
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST是一个类字典对象
        # 通过关键字获取提交Choice的id,字符串格式
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # 若该问题中找不到choice的id抛出异常
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # 若找到了则该选项的投票数加1
        selected_choice.votes += 1
        selected_choice.save()
        # 将请求重定向到Question的结果界面
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
