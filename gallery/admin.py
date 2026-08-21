from django.contrib import admin
from gallery.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada") #cria as colunas, para maior organizacao
    list_display_links = ("id", "nome") #faz com que os campos selecionados sejam links clicáveis   
    search_fields = ("nome",) #possibilita a pesquisa, no caso, pelo nome | este campo deve ser um tupla ou uma lista
    list_filter = ("categoria",) #listra de filtros
    list_editable = ("publicada",)
    list_per_page = 10 #paginacao, 10 itens por paginas

admin.site.register(Fotografia, ListandoFotografias) #registra o nosso database 
