from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required

class LoginViews(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            form = AuthenticationForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)
    def post(self,request):
        form = AuthenticationForm(request=request,data=request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            print(password)
            user = authenticate(request, username=username,password=password)
            print(user.username)
            if user is not None:
                login(request,user)
                messages.success(request, "you Login Successfully", "success")
                return redirect('Blog:blog')

        return render(request, 'accounts/login.html', context)


        # return render(request,'accounts/login.html',context={"form":auth_form})


# @login_required(login_url="/accounts/login/")

class LogoutViews(View):
    @method_decorator(login_required)
    def get(self,request):
        logout(request)
        messages.warning(request, "you Logout Successfully", "danger")
        return redirect('Blog:blog')
class SingupViews(View):
    def get(self,request):
        if not request.user.is_authenticated:
            form = UserCreationForm()
            context = {'form': form}
            return render(request,'accounts/singup.html',context)
        else:
            return redirect('/')
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "you Account Create Successfully", "success")
            return redirect('Blog:blog')
        context = {'form': form}
        return render(request, 'accounts/singup.html', context)
# Shahin37