# Generated by Django 4.1 on 2022-08-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_bolao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='resultado',
            field=models.CharField(default='Esperando o jogo', max_length=200),
        ),
    ]
