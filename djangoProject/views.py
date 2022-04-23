from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


def index(request, year):
    print(year)
    return HttpResponse('菜鸟教程')


def index1(request, year, month):
    print(year, '-', month)
    return HttpResponse('菜鸟教程')


def get_request(request):
    name = request.GET.get("name")
    return HttpResponse('姓名：{}'.format(name))


@csrf_exempt
def post_request(request):
    name = request.POST.get("name")
    return HttpResponse('姓名：{}'.format(name))


def other_request(request):
    name = request.body
    print(name)
    path = request.path
    print(path)
    method = request.method
    print(method)
    return HttpResponse("菜鸟教程")


def redirect_request(request):
    return redirect('/runoob/')


def hello(request):
    return HttpResponse("Hello world!")


def runoob(request):
    # context = {}
    # context['hello'] = 'helloWorld!'
    # return render(request, 'runoob.html', context)
    hello = "Helloworld!"
    views_name = ["菜鸟教程1", "菜鸟教程2","菜鸟教程3",]
    name_dict = {"name":"hzh", "age":25,}
    bl = 0
    num = 1024 * 1024
    time = datetime.now()
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, "runoob.html", {"hello":hello,
                                           "name":views_name,
                                           "name_dict":name_dict,
                                           "bl":bl,
                                           "num":num,
                                           "time":time,
                                           "views_str":views_str,})