# Generated by Django 2.2.4 on 2021-04-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0002_auto_20210429_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectos',
            name='estado',
            field=models.CharField(choices=[('0', 'Parado'), ('1', 'Concluido')], default='prado', max_length=100),
        ),
    ]