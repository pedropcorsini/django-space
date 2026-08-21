from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#rotas -> apps 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls')), #importa o urlpatterns do app gallery (para maior organizacao e boa pratica de programacao) tirou a responsabilidade do setup de citar todas as rotas.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #indica pro django que ele precisa utilizar as referencias indicadas no settings.py

