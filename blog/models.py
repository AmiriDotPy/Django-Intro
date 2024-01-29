from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    counted_view = models.IntegerField(default = 0)
    status = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    publish_at = models.DateTimeField(null = True)
    # image
    # author_id
    # post_categorys
    # post_tags
