from django import template
from blog.models import Post , Category
from django.utils import timezone
register = template.Library()


@register.inclusion_tag('blog/latest-posts.html')
def LatestPosts(arg = 2):
    posts = Post.objects.filter(status = 1).order_by('publish_at')[:arg]
    return {'posts' : posts}



@register.inclusion_tag('blog/popular-posts.html')
def PopularPosts(arg = 2):
    posts = Post.objects.filter(status = 1).order_by('-counted_view')[:arg]
    return {'posts' : posts}

@register.inclusion_tag('blog/blog-post-categoreis.html')
def PostCategory():
    posts = Post.objects.filter(status = 1)
    categoreis = Category.objects.all()
    cat_dict = {}
    for name in categoreis:
        cat_dict[name] = posts.filter(post_categorys = name).count()
    return {'categoreis' : cat_dict}

@register.inclusion_tag('website/website-latest-posts.html')
def MainPageLatestPosts(arg = 2):
    posts = Post.objects.filter(publish_at__lt = timezone.now(),status = 1).order_by('publish_at')[:arg]
    return {'posts' : posts}