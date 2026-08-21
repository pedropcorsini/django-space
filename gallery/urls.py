from django.urls import path
from gallery.views import index, imagem, buscar

#boa logica de programacao, criar lista com os urls:
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]