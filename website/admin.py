from django.contrib import admin
from .models import *

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title' , 'created_at' , 'updated_at' , 'publish_at']
    list_filter = ['created_at']

# admin.site.register(Post , PostAdmin)
    


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'created_at']
    list_filter = ['email']

# admin.site.register(Post , ContactAdmin)