# Generated by Django 2.2.4 on 2021-04-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step', '0005_projectos_projecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectos',
            name='projecto',
            field=models.FileField(default=None, upload_to='Projectos'),
        ),
    ]
