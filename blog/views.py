from django.shortcuts import render ,get_object_or_404
from django.utils import timezone
from .models import Post , Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def Counter(pid):
    post = get_object_or_404(Post.objects.exclude(publish_at__gt = timezone.now()), status = 1,id=pid)
    post.counted_view += 1
    post.save()


def LoadBlogSingle(request , pid):
    Counter(pid)
    post = get_object_or_404(Post.objects.exclude(publish_at__gt = timezone.now()), status = 1,id=pid)
    nextPost = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__gt = pid).first()
    previousPost = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__lt = pid).last()
    context = {'post' : post ,'nextpost' : nextPost , 'previouspost' : previousPost }
    return render(request, 'blog/single.html' ,context)


def LoadBlog(request, cat_name = None , author_username = None):
    tags = Tag.objects.all()
    posts = Post.objects.filter(publish_at__lt = timezone.now(), status = 1)
    if cat_name:
        posts = posts.filter(post_categorys__name = cat_name)
    if author_username:
        posts = posts.filter(author__username = author_username)
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts' : posts , 'tags' : tags}
    return render(request, 'blog/blog.html' , context)


def BlogCategoreis(request, cat):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(post_categorys__name = cat)
    context = {'posts' : posts}
    return render(request, 'blog/blog.html' , context)

 
def Blog_Search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
       if s:= request.GET.get('s'):
            posts =  posts.filter(content__contains = s)
    context = {'posts' : posts}
    return render(request , 'blog/blog.html' , context)