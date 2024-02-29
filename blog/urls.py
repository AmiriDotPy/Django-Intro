from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path('<int:pid>' , views.LoadBlogSingle , name = 'single'),
    path('' , views.LoadBlog , name = 'index'),
    path('category/<str:cat_name>' , views.LoadBlog , name = 'category'),
    path('author/<str:author_username>' , views.LoadBlog , name = 'author'),
    path('search/' , views.Blog_Search , name = 'search'),
]