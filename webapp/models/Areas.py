from django.db import models
from django.contrib.auth.models import User


class Areas(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, unique=True)
    subtitulo = models.TextField(null=True, blank=True, default='')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    atualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Áreas"
