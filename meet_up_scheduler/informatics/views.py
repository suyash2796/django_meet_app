from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from django.forms import modelform_factory

from .models import Seminar

MeetupForm = modelform_factory(Seminar, exclude = [])

# Create your views here.
def meetup_detail(request, id):
    meetup =  get_object_or_404(Seminar, pk=id)
    return render(request,"informatics/meetup.html",{"meetup":meetup})

def get_cities(request):
    return render(request,"informatics/cities.html",{"cities":Seminar.objects.all()})

def new_meetup(request):
    if request.method == "POST":
        form = MeetupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:            
        form  = MeetupForm()
    return render(request,"informatics/new_meetup.html", {'form':form})

