from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello world</h1>")


def home(request):
    return render(request, 'home.html', {'name':'Tuan'})
