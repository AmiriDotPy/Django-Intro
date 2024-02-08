from django.shortcuts import render , get_object_or_404
from .models import Post
from django.utils import timezone




def Counter(pid):
    post = get_object_or_404(Post.objects.exclude(publish_at__gt = timezone.now()),status = 1,id=pid)
    post.counted_view += 1
    post.save()


def LoadBlogSingle(request , pid):
    Counter(pid)
    post = get_object_or_404(Post.objects.exclude(publish_at__gt = timezone.now()),status = 1,id=pid)
    nextPost = get_object_or_404(Post.objects.exclude(publish_at__gt = timezone.now()),status = 1, id__gt = pid)
    # nextPost = getNextPosts.first()
    previousPost = get_object_or_404(Post.objects.exclude(publish_at__gt = timezone.now()),status = 1,pk__lt = pid)
    # previousPost = GetPreviousPosts.first()
    context = {'post' : post , 'nextpost' : nextPost , 'previouspost' : previousPost}
    return render(request, 'blog/single.html' ,context)


def LoadBlog(request):
    posts = Post.objects.exclude(publish_at__gt = timezone.now() , status = 1)
    context = {'posts' : posts}
    return render(request, 'blog/blog.html' , context)



 
