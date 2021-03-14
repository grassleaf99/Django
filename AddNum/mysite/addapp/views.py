from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello world</h1>')


def getnum(request):
    return render(request, 'getnum.html')


def tinhtong(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'resultAdd.html', {'result':res})


def tinhnhan(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 * val2
    return render(request, 'resultMul.html', {'result': res})
