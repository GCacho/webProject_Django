from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"webProjectApp/home.html")


def servicios(request):
    return render(request,"webProjectApp/servicios.html")


def tienda(request):
    return render(request,"webProjectApp/tienda.html")


def blog(request):
    return render(request,"webProjectApp/blog.html")


def contacto(request):
    return render(request,"webProjectApp/contacto.html")
