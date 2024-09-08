from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)


    def lastmod(self, obj):
        return obj.publish_date

    def location(self,item):
        return reverse('Blog:blog-single',kwargs={'Pid': item.id})

