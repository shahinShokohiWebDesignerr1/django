from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class HomeView(View):
    def get(self,request):
        return HttpResponse('this is a test')
class AboutView(View):
    def get(self,request):
        return HttpResponse('this is a about')