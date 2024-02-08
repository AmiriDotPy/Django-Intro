from django.shortcuts import render , get_object_or_404
from .models import Post
from django.utils import timezone




def Counter(pid):
    post = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , pk = pid)
    post.counted_view += 1
    post.save()


def LoadBlogSingle(request , pid):
    Counter(pid)
    post = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , pk = pid)    
    nextPost =  Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__gt = pid).first()
    previousPost = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__lt = pid).first()
    context = {'post' : post , 'nextpost' : nextPost , 'previouspost' : previousPost}
    return render(request, 'blog/single.html' ,context)


def LoadBlog(request):
    posts = Post.objects.filter(publish_at__lt = timezone.now(), status = 1)
    context = {'posts' : posts}
    return render(request, 'blog/blog.html' , context)



 
