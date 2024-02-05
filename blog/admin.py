from django.contrib import admin
from .models import *


# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title' ,'author', 'created_at' , 'updated_at' , 'publish_at']
    list_filter = ['created_at' , 'author']

# admin.site.register(Post , PostAdmin)
