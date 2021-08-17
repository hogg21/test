from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse('<h1>Hogg programmer</h1>')

def home(response):
    return HttpResponse('<h1>view 1</h1>')