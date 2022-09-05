from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from .forms import FormularioContacto


# Create your views here.
def contacto(request):
    formulario_contacto= FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST) # Para mas info https://youtu.be/_BOOv6GK-68
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre") # Los nombres vienen de forms.py
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage( # Para mas info: https://youtu.be/J0_RYvw3SlY
                "Mensaje desde Django",
                f"El usuario: {nombre} con la direccion: {email} envio el siguiente correo: {contenido}",
                ["guillermo.cacho.v@gmail.com"],
                reply_to=[email]
            ) 
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request,"contacto/contacto.html", {'miFormulario':formulario_contacto})