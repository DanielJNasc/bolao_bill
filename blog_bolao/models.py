from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Jogo(models.Model):
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_1 = models.CharField(max_length=200)
    time_2 = models.CharField(max_length=200)
    estadio = models.TextField()
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_do_jogo = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.time_1} X {self.time_2}'
