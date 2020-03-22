from django.http import HttpResponse

# 视图
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
