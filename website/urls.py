from django.urls import path 
from . import views

app_name = "website"

urlpatterns = [
    path('' , views.LoadIndex , name = 'index'),
    path('about/' , views.LoadAbout , name = 'about'),
    path('contact/' , views.LoadContact , name = 'contact'),
]