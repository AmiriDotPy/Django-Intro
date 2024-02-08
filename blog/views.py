from django.shortcuts import render 
from django.utils import timezone
from .models import Post
from django.http import Http404







def Counter(pid):
    post = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , pk = pid).first()
    post.counted_view += 1
    post.save()

def NextPost(pid):
    return  Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__gt = pid).first()
def PreviousPost(pid):
    return Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__lt = pid).last()


def LoadBlogSingle(request , pid):
    try:
        Counter(pid)
        post = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id = pid).first()
        nextPost = NextPost(pid)
        previousPost =PreviousPost(pid)
        context = {'post' : post , 'nextpost' : nextPost , 'previouspost' : previousPost}
    except Post.DoesNotExist:
        raise Http404('page not found')
    return render(request, 'blog/single.html' ,context)


def LoadBlog(request):
    posts = Post.objects.filter(publish_at__lt = timezone.now(), status = 1)
    context = {'posts' : posts}
    return render(request, 'blog/blog.html' , context)



 
