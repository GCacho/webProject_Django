# Para mas info: https://youtu.be/UJfuqCefRxc
from django.urls import path

from . import views

urlpatterns = [
    path('',views.blog, name='Blog'),
]
