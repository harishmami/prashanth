from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def home(request):
    context = {"name": "siva", "age": 30,
               "education": [{"type": "School", "name": "Nagarjuna", "percent":86.6},
                             {"type": "Intermediate", "name": "Narayana", "percent":94.1},
                             {"type": "Btech", "name": "KORM", "percent":71.1}]
               }
    return render(request, "polls/home.html", context)