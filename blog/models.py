from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    title = models.CharField(max_length=400)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/images/img/',default="blog/images/default/default.jpg")
    login_required = models.BooleanField(default=False)
    count_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_at"]

    def get_absolute_url(self):
        return reverse('Blog:blog-single',kwargs={'Pid': self.id})

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField(null=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-created_at',)

    # def tester(self):
    #     res = self.title + "25456456"
    #     return res

