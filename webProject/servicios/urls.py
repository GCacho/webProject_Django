# Para mas info: https://youtu.be/PRdrrxCggIU
from django.urls import path
from . import views

urlpatterns = [
    path('',views.servicios, name='Servicios'),
]