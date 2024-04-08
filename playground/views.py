from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello form my django + dipoo +sahoo")


# Create your views here.
