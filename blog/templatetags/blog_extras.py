from django import template
from blog.models import Post,Category,Comment

register = template.Library()

@register.simple_tag(name='res')
def res():
    post = Post.objects.filter(status=1).count()
    return post
@register.filter()
def snippet(value,arg = 50):
    return value[:arg] + "..."
@register.inclusion_tag('blog/popularpost.html')
def latest_post(arg = 3):
    posts = Post.objects.filter(status = 1).order_by('-publish_date')[:arg]
    return {"posts": posts}
@register.inclusion_tag('blog/blog_post_category_count.html')
def PostCountCategories():
    posts = Post.objects.filter(status = 1)
    categories= Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}

@register.simple_tag(name='comments_counts')
def res(pid):
    blog_single = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=blog_single.id, approved=True).count()
