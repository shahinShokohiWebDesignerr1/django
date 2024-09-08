
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm,NewsLetterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'website/index.html')
class AboutView(View):
    def get(self, request):
        return render(request, 'website/about.html')
class ContactView(View):
    def get(self,request):
        forms = ContactForm()
        return render(request, 'website/contact.html', {'form': forms})
    def post(self,request):
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "your message submit successfully","success")
        else:
            messages.error(request, "check again and try again","danger")
            return redirect('website:contact')
        return render(request, 'website/contact.html', {'form': forms})

class NewsLetterView(View):
        def get(self, request):
            return HttpResponseRedirect('/')
        def post(self,request):
            form = NewsLetterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
