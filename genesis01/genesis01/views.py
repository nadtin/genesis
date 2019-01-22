from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def videos(request):
    return render(request, 'videos.html')

def lab(request):
    return render(request, 'lab.html')