from django.shortcuts import render , get_object_or_404
from .models import Post
from datetime import  datetime


def Counter(pid):
        post = get_object_or_404(Post,id=pid)
        post.counted_view += 1
        post.save()


def LoadBlogSingle(request , pid):
    post = get_object_or_404(Post,id=pid)
    Counter(pid)
    context = {'post' : post}
    return render(request, 'blog/single.html' ,context)


   


def LoadBlog(request):
    posts = Post.objects.exclude(publish_at__gt = datetime.today()).exclude(status = 0)
    context = {'posts' : posts}
    return render(request, 'blog/blog.html' , context)

