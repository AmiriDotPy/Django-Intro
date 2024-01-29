from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'created_at']
    list_filter = ['email']

# admin.site.register(Post , ContactAdmin)