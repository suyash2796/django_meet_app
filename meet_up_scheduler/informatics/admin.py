from django.contrib import admin

# Register your models here.

from .models import Seminar, City
admin.site.register(Seminar)
admin.site.register(City)
