from django.shortcuts import render
from .models import *
def show(request):
    carts = Cart.objects.all()
    return render(request, 'show.html', {'carts':carts})
