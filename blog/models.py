from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self) -> str:
        return self.name
            
class Tag(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User,on_delete = models.SET_NULL , null = True)
    content = models.TextField()
    counted_view = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    publish_at = models.DateTimeField(null = True)
    image = models.ImageField(upload_to=  'blog/' , default='blog/default.jpg')
    post_categorys = models.ManyToManyField(Category)
    post_tags = models.ManyToManyField(Tag)

    def snippets(self):
        return self.content[:100] + '...'

