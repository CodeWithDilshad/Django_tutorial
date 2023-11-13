from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Home(request): 
    return render (request, 'index.html')


def page1(request):
    return HttpResponse("This is page 1.")