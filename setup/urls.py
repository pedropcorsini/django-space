from django.contrib import admin
from django.urls import path, include

#rotas -> apps 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')), #importa o urlpatterns do app gallery (para maior organizacao e boa pratica de programacao) tirou a responsabilidade do setup de citar todas as rotas.
]
