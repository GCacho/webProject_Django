from django.urls import path

from webProjectApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='Home'),
    path('tienda/',views.tienda, name='Tienda'),
    path('contacto/',views.contacto, name='Contacto'),
    # Para mas info: https://youtu.be/UJfuqCefRxc
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Para mas info: https://youtu.be/kBsj5xLuuoY