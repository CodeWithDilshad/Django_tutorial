from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Home(request): 
    people=[
        {'name':"Ansari Dilshad", 'age':23},
        {'name':"Ansari Irshad", 'age':24},
        {'name':"Md Arshad", 'age':25},
        {'name':"Umar Farooq", 'age':45},
        {'name':"Mohd Shad", 'age':30},
        {'name':"Mr. Gupta", 'age':63},
    ]

    vegatables=['baigan','aaloo','gobhi']


    return render (request, 'home/index.html', context={'people':people, 'text':vegatables})


def contact(request):
    
    return render(request, 'home/contact.html')


def about(request):
    return render (request, 'home/about.html')