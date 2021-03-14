from django.urls import path

from . import views

urlpatterns = [
    path('static', views.index, name='index'),
    path('dynamic', views.home, name='home')
]