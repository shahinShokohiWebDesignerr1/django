from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,'website/home.html')
class AboutView(View):
    def get(self, request):
        return render(request, 'website/about.html')
class ContactView(View):
    def get(self,request):
        return render(request,'website/contact.html')