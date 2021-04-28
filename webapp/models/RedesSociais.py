from django.db import models
from django.contrib.auth.models import User

class RedesSociais(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    iconName = models.CharField(max_length=20, null=True, blank=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    criadoPor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.dataCriacao}'

    class Meta:
        verbose_name_plural = "Redes Sociais"
