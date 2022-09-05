from django.urls import path

from . import views

urlpatterns = [
    path('',views.tienda, name='Tienda'), # Para mas info: https://youtu.be/1GPBCwhNISw
]
