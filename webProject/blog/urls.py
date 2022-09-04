# Para mas info: https://youtu.be/UJfuqCefRxc
from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog, name='Blog'), # -> base.html
    path('categorias/<int:categoria_id>/', views.categoria, name="categorias") # -> URL Insertada
]
