from django.db import models
from django.contrib.auth.models import User
from .Areas import Areas


class Slides(models.Model):
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    imagem = models.ImageField(default='default.jpg', upload_to='SlidesImg')
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataAtualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.area.nome}'

    class Meta:
        verbose_name_plural = "Slides"
