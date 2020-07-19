
from django.urls import path

##importing my view
from .views import meetup_detail, get_cities

urlpatterns = [
    path('cities', get_cities, name = 'cities' ),
    path('<int:id>', meetup_detail, name = "meet"),
]
