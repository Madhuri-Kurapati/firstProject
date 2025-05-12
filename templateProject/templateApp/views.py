from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home_view(request):


    l=['quotes 1','quotes 2','quotes 3','quotes 4','quotes 5',]
    choice=random.choice(l)
    d={'quote':choice}
    return render(request,'templateApp/template.html',context=d)
