from django.shortcuts import render
from servicios.models import Servicio # Para mas info 1 => https://youtu.be/Dsgsfnp8RA8 - 2=> https://youtu.be/PRdrrxCggIU

# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request,"servicios/servicios.html", {"servicios":servicios})




