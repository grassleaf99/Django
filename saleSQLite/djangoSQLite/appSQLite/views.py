from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=pass1, email=email, first_name=firstname, last_name=lastname)
            user.save()
            print('user created')
            return redirect('login')
    else:
        return render(request, 'register.html')

#tai khoan username: namt pass: 443
#tai khoan username : hieu pass: 234
#tai khoan username: 654 pass: 17
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'successLI.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
