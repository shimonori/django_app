from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from  .forms import LoginForm
from  .forms import notLoginForm
import subprocess


# Create your views here.




class IndexView(TemplateView):

    def __init__(self):
        self.params = {
        'title': 'ログインしてください',
        'form': LoginForm(),
        }
    
    def get(self, request):
        return render(request, 'try_app/index.html', self.params)

    def post(self, request):
        print("post")

        return render(request, 'try_app/index.html', self.params)

class notLoginView(TemplateView):

    def __init__(self):
        self.params = {
        'title': 'パスワードリセット',
        'h1': '登録したメールアドレスを入力してください',
        'form': notLoginForm(),
        }

    def get(self, request):
        return render(request, 'try_app/notLogin.html', self.params)

    def post(self, request):
        self.params = {
            'title': 'パスワードリセット',
            'p': '登録されたメールアドレスにリセット用のメールを送信いたしました。',
        }
        cmd = "python try_app/mail/mail_smtp.py " + request.POST['mail']
        print(cmd)
        subprocess.call(cmd.split())
        return render(request, 'try_app/sendmail_complete.html', self.params)
