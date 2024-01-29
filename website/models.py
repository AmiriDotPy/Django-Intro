from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    email = models.EmailField()
    massage = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)