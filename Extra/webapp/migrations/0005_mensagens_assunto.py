# Generated by Django 2.2.4 on 2021-03-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_mensagens_lida'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagens',
            name='assunto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]