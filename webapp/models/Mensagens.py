from django.db import models
from django.contrib.auth.models import User
from .Servicos import Servicos


class Mensagens(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    numeroTelefone = models.CharField(max_length=20, null=True, blank=True)
    interesse = models.ForeignKey(Servicos, on_delete=models.SET_NULL, null=True, default=None)
    assunto = models.CharField(max_length=50, null=True, blank=True)
    mensagem = models.TextField(null=True, blank=True)
    lida = models.BooleanField(default=False)
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.dataCriacao}'

    class Meta:
        verbose_name_plural = "Mensagem da página contactos"
