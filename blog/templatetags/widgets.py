from django import template
from blog.models import Post
register = template.Library()


@register.inclusion_tag('blog/latest-posts.html')
def LatestPosts(arg = 2):
    posts = Post.objects.filter(status = 1).order_by('publish_at')[:arg]
    return {'posts' : posts}



@register.inclusion_tag('blog/popular-posts.html')
def PopularPosts(arg = 2):
    posts = Post.objects.filter(status = 1).order_by('-counted_view')[:arg]
    return {'posts' : posts}