from django.shortcuts import render, get_object_or_404
from gallery.models import Fotografia

def index(request): #rota principal.
    #fotografias = Fotografia.objects.all() #vai trazer uma lista com todos os objetos que estao dentro do nosso model
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) #filtra no banco as imagens mais recentes e as imagens que estao com o bool publicada = True (ativadas) | colocando '-' antes no order_by, inverte a ordem
    return render(request, 'gallery/index.html', {'cards': fotografias}) #render permite o envio de algumas informacoes como dict

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #pk -> primary key
    return render(request, 'gallery/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) #puxa todos osn itens do banco de dados

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #busca se existe, dentro do nome que estamos conferindo, se existe alguma parte que faz sentido (exemplo, gal faz match com galaxia)
        

    return render(request, "gallery/buscar.html", {"cards": fotografias})
