from django.db import models

# Create your models here.
class Veiculo(models.Model):
    placa = models.CharField(max_length=30)
    modelo = models.CharField(max_length=11)
    cor = models.CharField(max_length=12)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.placa

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)


    def __str__(self):
        return self.nome


