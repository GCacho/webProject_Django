from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"webProjectApp/home.html")

def tienda(request):
    return render(request,"webProjectApp/tienda.html")