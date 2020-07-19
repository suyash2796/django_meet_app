from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from .models import Seminar

# Create your views here.
def meetup_detail(request, id):
    meetup =  get_object_or_404(Seminar, pk=id)
    return render(request,"main_web/meetup.html",{"meetup":meetup})
