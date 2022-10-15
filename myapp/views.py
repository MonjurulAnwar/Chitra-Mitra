from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
   # return HttpResponse("Hi,This is home page")

def Home(request):
    return render(request,'Home.html')

def Download(request):
    return render("Download.html")

def Search(request):
    return render("Search.html")