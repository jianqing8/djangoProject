from django.shortcuts import render
from django.http import HttpResponse  # 加入引用


# Create your views here.
def test(request):
    return HttpResponse("hello test")  # 返回 HttpResponse 响应函数


def login(request):
    return render(request, 'login.html')
# Create your views here.
