from django.db import models
from django.contrib.auth.models import User
from .Actividades import Actividades


class ActividadesLink(models.Model):
    actividade = models.ForeignKey(Actividades, on_delete=models.CASCADE)
    link = models.CharField(max_length=200, null=False, blank=False)
    dataCriacao = models.DateTimeField(
        verbose_name='Data. Criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField(
        verbose_name='Data. Atualização', auto_now=True)

    def __str__(self):
        return f'{self.actividade.titulo} - {self.link}'

    class Meta:
        verbose_name_plural = "Link de Vídeos das Actividades"
