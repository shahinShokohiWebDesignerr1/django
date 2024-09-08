
from django.urls import path
from blog.feeds import LatestEntriesFeed
from .views import BlogHomeView,BlogSingleView,BlogCategoryView,BlogSearchView
app_name = 'Blog'
urlpatterns = [
    path('', BlogHomeView.as_view(),name = 'blog'),
    path('blog_detail/<int:Pid>/', BlogSingleView.as_view(),name = 'blog-single'),
    path('blog_category/<str:cat_name>/', BlogHomeView.as_view(),name = 'blog-category'),
    path('tag/<str:tag_name>/', BlogHomeView.as_view(),name = 'tag'),
    path('tag/<str:tag_name>/', BlogHomeView.as_view(),name = 'tag'),
    path('search/', BlogSearchView.as_view(),name = 'blog-search'),
    path('blog_author/<str:author_username>/', BlogHomeView.as_view(),name = 'blog-author'),
    path("rss/feed/", LatestEntriesFeed()),
    # path('test/', ResView.as_view()),
]
