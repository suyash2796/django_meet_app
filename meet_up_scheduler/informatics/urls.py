
from django.urls import path

##importing my view
from .views import meetup_detail, get_cities, new_meetup

urlpatterns = [
    path('cities', get_cities, name = 'cities' ),
    path('<int:id>', meetup_detail, name = "meet"),
    path('new_meetup', new_meetup, name = "new_meetup"),
]
