from django.shortcuts import render 
from django.utils import timezone




def Counter(pid):
    post = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , pk = pid).first()
    post.counted_view += 1
    post.save()

def NextPost(pid):
    return  Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__gt = pid).first()
def PreviousPost(pid):
    return Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id__lt = pid).last()


def LoadBlogSingle(request , pid):
    Counter(pid)
    post = Post.objects.filter(publish_at__lt = timezone.now(), status = 1 , id = pid).first()
    nextPost = NextPost(pid)
    previousPost =PreviousPost(pid)
    context = {'post' : post , 'nextpost' : nextPost , 'previouspost' : previousPost}
    return render(request, 'blog/single.html' ,context)


def LoadBlog(request):
    posts = Post.objects.filter(publish_at__lt = timezone.now(), status = 1)
    context = {'posts' : posts}
    return render(request, 'blog/blog.html' , context)



 
