from typing import Any
from .forms import SignUpForm,LoginForm
from django.contrib.auth import login,views,authenticate
from django.contrib.auth.views import LogoutView,LoginView as BaseLoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import CreateView,TemplateView
from django.views import View
from django.urls import reverse_lazy

# Create your views here.

class SignupView(CreateView):
    # return render(request, 'signup.html', {'somedata':100})
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:redirect')
    # TODO ログイン後の遷移処理の追加(pathなど)

    def get(self, request, *args, **kwargs):
        # すでにログインしている場合は新しいログインを許可しない
        if self.request.user.is_authenticated:
            return self.already_logged_in_response()

        return super().get(request, *args, **kwargs)

    def already_logged_in_response(self):
        # すでにログインしている場合のリダイレクト先やメッセージをここで指定
        return HttpResponseRedirect(reverse_lazy('accounts:redirect'))

    def form_valid(self, form: BaseModelForm):
        # response = super().form_valid(form)
        # user = authenticate("email")
        user = form.save()
        login(self.request,user) # ログイン維持の処理
        self.object = user

        # return response
        return HttpResponseRedirect(self.get_success_url()) 

class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    def get(self, request, *args, **kwargs):
        # すでにログインしている場合は新しいログインを許可しない
        if self.request.user.is_authenticated:
            return self.already_logged_in_response()

        return super().get(request, *args, **kwargs)

    def already_logged_in_response(self):
        # すでにログインしている場合のリダイレクト先やメッセージをここで指定
        return HttpResponseRedirect(reverse_lazy('accounts:redirect'))

class LogoutView(LogoutView):
    template_name = 'accounts:logout'

class IndexView(TemplateView):
    template_name = 'accounts/index.html'

@login_required
def redirect(reqest): # redirect宣言後の遷移先
    return render(reqest, 'accounts/redirect.html')