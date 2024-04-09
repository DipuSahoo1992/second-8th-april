from django.shortcuts import render
from django.http import HttpResponse

book = {"name": "herry", "published at": 1775, "author": "dipoo sahoo"}



def hello(request):
    return render(request, "index.html", {"mylist":book})
