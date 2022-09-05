from django.shortcuts import render

# Create your views here.
def tienda(request): # Para mas info: https://youtu.be/1GPBCwhNISw
    return render(request,"tienda/tienda.html")