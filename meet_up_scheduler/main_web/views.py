from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from informatics.models import Seminar

# Create your views here.
def greet(request):
    return render(request,"main_web/index.html", {"nu_seminars":Seminar.objects.count()
    ,'seminars': Seminar.objects.all()
    })

def get_current_time(request):
    return HttpResponse("Welcome! currrent time is : "+ str(datetime.now()))