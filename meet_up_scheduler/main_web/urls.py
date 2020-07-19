
from django.urls import path

##importing my view
from .views import greet, get_current_time

urlpatterns = [
    path('', greet, name = 'home'),
    path('now', get_current_time ),
]
