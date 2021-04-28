from django.db import models
from django.contrib.auth.models import User


class Sobre(models.Model):
    titulo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    criadoPor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.subTitulo}'

    class Meta:
        verbose_name_plural = "Sobre"
