from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def greet(request):
    return HttpResponse("Hi, Welcome to the meetup!!")

def get_current_time(request):
    return HttpResponse("Welcome! currrent time is : "+ str(datetime.now()))