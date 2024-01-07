from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.LoadIndex),
    path('about/' , views.LoadAbout),
    path('contact/' , views.LoadContact),
]