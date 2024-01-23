from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path('single/' , views.LoadBlogSingle , name = 'single'),
    path('' , views.LoadBlog , name = 'blog'),
]