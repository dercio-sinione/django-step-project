# Generated by Django 2.2.4 on 2021-03-24 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('subTitulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subtítulo')),
                ('objectivos', models.TextField(blank=True, null=True, verbose_name='Objectivos')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('localizacao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Localização')),
                ('imagem', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='ActividadesImg')),
                ('dataInicio', models.DateField(blank=True, default='', null=True, verbose_name='Data. Início')),
                ('dataTermino', models.DateField(blank=True, default='', null=True, verbose_name='Data. Termino')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data. Criação')),
                ('dataAtualizacao', models.DateTimeField(auto_now=True, verbose_name='Data. Atualização')),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('subtitulo', models.TextField(blank=True, null=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Áreas',
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('conteudo', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(default='default.jpg', upload_to='ServicosImg')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Serviços',
                'ordering': ('-criadoPor',),
            },
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subTitulo', models.CharField(blank=True, max_length=50, null=True)),
                ('conteudo', models.TextField()),
                ('imagem', models.ImageField(default='default.jpg', upload_to='SobreImg')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sobre',
            },
        ),
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(default='default.jpg', upload_to='SlidesImg')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Areas')),
            ],
            options={
                'verbose_name_plural': 'Slides',
            },
        ),
        migrations.CreateModel(
            name='ServicosDetalhes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('conteudo', models.TextField()),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Servicos')),
            ],
            options={
                'verbose_name_plural': 'Detalhes de Serviços',
            },
        ),
        migrations.CreateModel(
            name='RedesSociais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('iconName', models.CharField(blank=True, max_length=20, null=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Redes Sociais',
            },
        ),
        migrations.CreateModel(
            name='Projectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('subTitulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subtítulo')),
                ('objectivos', models.TextField(blank=True, null=True)),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('metas', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(default='default.jpg', upload_to='ProjectosImg')),
                ('dataInicio', models.DateField(default='', verbose_name='Data. Início')),
                ('dataTermino', models.DateField(default='', verbose_name='Data. Termino')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projectos',
            },
        ),
        migrations.CreateModel(
            name='MensagemContactos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('numeroTelefone', models.CharField(blank=True, max_length=20, null=True)),
                ('mensagem', models.TextField(blank=True, null=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('interesse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Servicos')),
            ],
            options={
                'verbose_name_plural': 'Mensagem da página contactos',
            },
        ),
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=20)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataAtualizacao', models.DateTimeField(auto_now=True)),
                ('criadoPor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='ActividadesLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('actividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Actividades')),
            ],
            options={
                'verbose_name_plural': 'Link de Vídeos das Actividades',
            },
        ),
    ]