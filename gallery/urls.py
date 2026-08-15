from django.urls import path
from gallery.views import index

#boa logica de programacao, criar lista com os urls:
urlpatterns = [
    path('', index)
]