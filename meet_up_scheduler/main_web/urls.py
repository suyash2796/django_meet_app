
from django.urls import path

##importing my view
from .views import greet, get_current_time, get_landing, get_about,get_contact

urlpatterns = [
    path('', greet, name = 'home'),
    path('now', get_current_time ),
    path('landing', get_landing, name = 'landing' ),
    path('about', get_about, name = 'about' ),
    path('contact', get_contact , name = 'contact'),
]
