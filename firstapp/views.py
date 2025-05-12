from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

# this is sample home view
def home_view(request):
    return  HttpResponse("<h1> This is my First Project </h1>")

def  second_view(request):
    time = datetime.datetime.now()
    formatted_time=time.strftime(f"%Y-%B-%d %H:%M ")
    return HttpResponse(f'<h2> time is{formatted_time}</h2>')

def third_view(request):
    name ='Madhuri'
    return HttpResponse(f'My name is {name}')