from django.shortcuts import render
from django.views import View
# Create your views here.
class BlogHomeView(View):
    def get(self,request):
        return render(request,'blog/blog-home.html')

class BlogSingleView(View):
    def get(self,request):
        return render(request,'blog/blog-single.html')