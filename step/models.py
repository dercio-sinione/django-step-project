from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# from django.urls import reverse

class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    imagem = models.ImageField(default='default.jpg',upload_to='ImgPerfil')

    def __str__(self):
        return f'Perfil - {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.imagem.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.imagem.path)

class Categorias(models.Model):
    nome = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nome}'

class Entidades(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    contacto = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'
    
class Projectos(models.Model):
    ops = [('Parado', 'Parado'),('Concluído', 'Concluído'), ('Em produção', 'Em produção')]
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100, default=None)
    custos = models.IntegerField(default='0')
    dataEntrega = models.DateField(default=None, null=True)
    dataRegisto = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=100, null=False, default='prado', choices=ops)
    projecto = models.FileField(upload_to='Projectos', default=None)
    progresso = models.IntegerField(default='0')
    dataConclusao = models.DateField(default=None, null=True, blank=True)
    entidade = models.ForeignKey(Entidades, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Notificacoes(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    categoria = models.CharField(max_length=100, null=False)
    projecto = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    # def __repr__(self):
    #     return f"Notificações('{self.titulo}','{self.idUser}')"