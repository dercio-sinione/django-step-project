# Generated by Django 2.2.4 on 2021-04-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectos',
            name='descricao',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
