from django.db import models
from django.contrib.auth.models import User
from webapp.models import Servicos


class ServicosDetalhes(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    conteudo = models.TextField(null=False, blank=False)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    criadoPor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.servico.nome} - {self.titulo}'

    class Meta:
        verbose_name_plural = "Detalhes de Serviços"
