from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hi")


def login(request):
    return HttpResponse("hi")

def logout(request):
    return HttpResponse("hi")

def register(request):
    return HttpResponse("hi")

def profile(request):
    return HttpResponse("hi")
