from django.http import HttpResponse
from django.shortcuts import render

# Create your views herev python functions.


def home(request):
    return HttpResponse("This Is Car MOdules")