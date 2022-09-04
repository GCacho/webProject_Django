from django.urls import path

from . import views

urlpatterns = [
    path('',views.contacto, name='Contacto'),
    # Para mas info: https://youtu.be/UJfuqCefRxc
]
