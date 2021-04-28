from django.db import models
from django.contrib.auth.models import User


class Endereco(models.Model):
    localizacao = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    tel1 = models.CharField(max_length=20, null=False, blank=False)
    tel2 = models.CharField(max_length=20, null=True, blank=True, default='')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    atualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.localizacao} - {self.dataCriacao}'

    class Meta:
        verbose_name_plural = "Endereços"
