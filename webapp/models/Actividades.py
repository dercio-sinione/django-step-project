from django.db import models
from django.contrib.auth.models import User


class Actividades(models.Model):
    titulo = models.CharField(verbose_name='Título',
                              max_length=50, null=False, blank=False)
    subTitulo = models.CharField(
        verbose_name='Subtítulo', max_length=50, null=True, blank=True)
    objectivos = models.TextField(
        verbose_name='Objectivos', null=True, blank=True)
    conteudo = models.TextField(
        verbose_name='Conteúdo', null=False, blank=False)
    localizacao = models.CharField(
        verbose_name='Localização', max_length=100, null=True, blank=True)
    imagem = models.ImageField(
        default='default.jpg', upload_to='ActividadesImg', blank=True, null=True)
    dataInicio = models.DateField(
        verbose_name='Data. Início', default='', blank=True, null=True)
    dataTermino = models.DateField(
        verbose_name='Data. Termino', default='', blank=True, null=True)
    dataCriacao = models.DateTimeField(
        verbose_name='Data. Criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField(
        verbose_name='Data. Atualização', auto_now=True)
    criadoPor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.subTitulo}'

    class Meta:
        verbose_name_plural = "Actividades"
