from django.db import models
from datetime import datetime
#ORM - django traduz entre o banco de dados e o python puro, no caso, as classes criadas
# Importante! = Toda vez que mudar os models, realize uma migration

class Fotografia(models.Model): 

    OPCOES_CATEGORIA = [ 
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ] #deve ser uma tupla - metodo charField entende tuplas

    #CharField = caractere | null=False = diz que nao pode ser um campo vazio | blank = algo como '', seguindo o msm principio de null=false
    nome = models.CharField(max_length=30, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=30, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False) #TextField = usado para grande campos de texto
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True) #pede o caminho para onde importar | pasta com ano, pasta com mes, pasta com dia para o caso de duplicatas
    publicada = models.BooleanField(default=False) #padrao = false (foto deve ser 'ativada')
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self): #metodo que retorna um str, no caso, o nome do item -> boa prática para visualizacao
        return self.nome