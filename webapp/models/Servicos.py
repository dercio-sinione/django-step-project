from django.db import models
from django.contrib.auth.models import User


class Servicos(models.Model):
    nome = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)
    imagem = models.ImageField(default='default.jpg', upload_to='ServicosImg')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    criadoPor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.dataCriacao}'

    class Meta:
        verbose_name_plural = "Serviços"
        ordering = ('-criadoPor',)
