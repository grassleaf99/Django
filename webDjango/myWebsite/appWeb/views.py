from django.shortcuts import render, redirect
from .models import Question, Choice
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
# ham authenticate giup xac thuc nguoi dung

# Create your views here.

class IndexClass(View):
    def get(self, request): # ham get co tac dung nhu khi nguoi dung get du lieu, cai nay hoat dong giong api get
    #def post(self, request): # ham get co tac dung nhu khi nguoi dung post du lieu, cai nay hoat dong giong api post
    # ngoai ra con co ca put, delete...
        return HttpResponse('<h2>Demo class base view</h2>')


def viewDB(request):
    question_list = Question.objects.all()
    choice_list = Choice.objects.all()
    dic = {'questions':question_list, 'choices':choice_list}
    return render(request, 'viewDB.html', dic)


def detailQuestion(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'question.html', {'qs':question})


def answer(request):
    try:
        choice_id = request.POST['mychoice']
        choice = Choice.objects.get(pk=choice_id)
        choice.vote += 1
        choice.save()
    except:
        return HttpResponse('<h2>Ban chua chon cau tra loi</h2>')
    return redirect('appweb:viewdb') # tham so cua redirect phai la name cua duong dan, duong dan nay co app_name la appweb o truoc


#@decorators.login_required(login_url='login/') # login_url nhan path den viec log in, path nay la path duoc nhac den trong file urls.py
def add_post(request):
    if request.method == 'POST':
        paFM = PostForm(request.POST)
        if paFM.is_valid():
            # khi thay doi lai quyen user can cache reload tu database user
            # de xem tat ca quyen cua user chay ham request.user.get_all_permissions()
            #print(request.user.get_all_permissions())
            #if request.user.has_perm('appWeb.add_post'): # ham has_perm() nhan ten app (trong file apps.py) roi . roi ten hoat dong roi _ roi ten model viet thuong
            paFM.save()
            return HttpResponse('<h2>Ban da luu 1 post moi</h2>')
            #else:
                #return HttpResponse('<h2>Ban ko co quyen luu post moi</h2>')
        else:
            return HttpResponse('<h2>Du lieu khong hop le, hay thu lai</h2>')
    else:
        aFM = PostForm()
        return render(request, 'addFormModels.html', {'aFM':aFM})

def email_handler(request):
    if request.method == 'POST':
        pse = SendEmail(request.POST)
        if pse.is_valid():
            tieude = pse.cleaned_data['title']
            mail = pse.cleaned_data['email']
            nd = pse.cleaned_data['content']
            check = pse.cleaned_data['cc']
            context = {'td':tieude, 'em':mail, 'ct':nd, 'c':check}
            #context = {'emailData': pse}
            return render(request, 'showSentEmail.html', context)
        else:
            return HttpResponse('<h2>Du lieu khong hop le, hay thu lai</h2>')
    else:
        se = SendEmail()
        return render(request, 'sendEmails.html', {'se':se})


class LoginClass(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('pass')
        user = authenticate(username=user_name, password=pass_word)
        if user is None:
            return HttpResponse('Ban vua an dang nhap %s %s nhung tai khoan do khong ton tai'%(user_name, pass_word))
        else:
            login(request, user)
            return render(request, 'successLogin.html')


class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('<h2>Ban chua dang nhap</h2>')
        else:
            return render(request, 'successLogin.html')


@decorators.login_required(login_url='login/') # login_url nhan path den viec log in, path nay la path duoc nhac den trong file urls.py
def demoDecorators(request):
    return HttpResponse('<h2>Ban xem duoc cai nay vi ban da qua dang nhap</h2>')

class DemoLoginRequiredMixin(LoginRequiredMixin, View):
    login_url = 'login/'
    def get(self, request):
        return HttpResponse('<h2>Ban xem duoc cai nay vi ban da qua dang nhap</h2>')
