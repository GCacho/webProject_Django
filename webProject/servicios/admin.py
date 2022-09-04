# Para mas informacion visitar: https://youtu.be/J5yKhrmMITQ
from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)