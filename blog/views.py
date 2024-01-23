from django.shortcuts import render

def LoadBlogSingle(request):
    return render(request, 'blog/single.html')


def LoadBlog(request):
    return render(request, 'blog/blog.html')

