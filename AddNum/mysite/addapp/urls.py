from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.index, name='index'),
    path('num', views.getnum, name='getnum'),
    path('sum', views.tinhtong, name='tong'),
    path('multication', views.tinhnhan, name='nhan')
]