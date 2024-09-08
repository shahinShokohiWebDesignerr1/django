from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from website.forms import ContactForm
from website.models import Contact
from .models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from blog.forms import CommentForm
# Create your views here.
class BlogHomeView(View):
    def get(self,request,**kwargs):
        posts = Post.objects.filter(status=1).all()
        if kwargs.get('cat_name'):
            posts = posts.filter(category__name=kwargs.get('cat_name'))
        if kwargs.get('author_username'):
            posts = posts.filter(author__username=kwargs.get('author_username'))
        if kwargs.get('tag_name'):
            posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        # pageination
        page = request.GET.get('page', 1)
        posts = Paginator(posts,3)
        try:
            posts = posts.page(page)
        except PageNotAnInteger:
            posts = posts.page(1)
        except EmptyPage:
            posts = posts.page(posts.num_pages)



        return render(request,'blog/blog-home.html',{'posts':posts})

class BlogSingleView(View):
    def get(self,request,Pid):
        posts = Post.objects.filter(status=1)
        blog_single = get_object_or_404(posts,pk = Pid,status = 1)
        if not blog_single.login_required :
            comments = Comment.objects.filter(post=blog_single.id,approved=True)[:7]
            form = CommentForm()
            context = {'post':blog_single,'comments':comments,'form':form}
            return render(request,'blog/blog-single.html',context)
        else:
            return redirect('Accounts:login')
    def post(self,request,Pid):
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, "your message submit successfully", "success")
        else:
            messages.error(request, "check again and try again", "danger")
        return redirect('Blog:blog')

# class ResView(View):
#     def get(self, request):
#         forms = ArticleForm()
#         return render(request, 'test.html', {'form': forms})
#
#     def post(self, request):
#         forms = ArticleForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             # messages.success(request, "Profile create successfully.","dark")
#             return redirect("Blog:blog")
#         return render(request, 'test.html', {'form': forms})

class BlogCategoryView(View):
    def get(self, request,cat_name):
        posts = Post.objects.filter(status = 1)
        posts = posts.filter(category__name = cat_name)
        return render(request,'blog/blog-home.html',{'posts':posts})

class BlogSearchView(View):
    def get(self, request):
        posts = Post.objects.filter(status=1)
        try:
            if request.method == 'GET':
                posts = posts.filter(content__contains=request.GET.get('s'))
        except:raise Http404
        return render(request,'blog/blog-home.html',{'posts':posts})
# class BlogContactView(View):
#     def get(self, request):
#         forms = ContactForm()
#         return render(request, 'website/contact.html', {'form': forms})


