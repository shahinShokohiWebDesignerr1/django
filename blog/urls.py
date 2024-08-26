
from django.urls import path
from .views import BlogHomeView,BlogSingleView
app_name = 'Blog'
urlpatterns = [
    path('', BlogHomeView.as_view(),name = 'blog'),
    path('blog_detail/', BlogSingleView.as_view(),name = 'blog-single'),

]
