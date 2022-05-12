from django.db import models

# Create your models here.


class Banda(models.Model):
    nome = models.CharField(max_length=255)
    em_atividade = models.BooleanField()

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.nome



class Integrante(models.Model):
    nome = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
