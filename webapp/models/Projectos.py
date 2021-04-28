from django.db import models
from django.contrib.auth.models import User


class Projectos(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=50, null=False, blank=False)
    subTitulo = models.CharField(verbose_name='Subtítulo', max_length=50, null=True, blank=True)
    objectivos = models.TextField(null=True, blank=True)
    conteudo = models.TextField(verbose_name='Conteúdo', null=False, blank=False)
    metas = models.TextField(null=True, blank=True)
    imagem = models.ImageField(default='default.jpg', upload_to='ProjectosImg')
    dataInicio = models.DateField(verbose_name='Data. Início', default='')
    dataTermino = models.DateField(verbose_name='Data. Termino', default='')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)
    criadoPor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.subTitulo}'

    class Meta:
        verbose_name_plural = "Projectos"
