from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Estadio(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.cidade}'

class Jogo(models.Model):
    TIPO_DE_FASE =(
        ('grupos', 'Fase de Grupos'),
        ('oitavas', 'Oitavas de final'),
        ('quartas', 'Quartas de final'),
        ('semi', 'Semi Final'),
        ('final', 'Final'),
    )
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_1 = models.CharField(max_length=200)
    time_2 = models.CharField(max_length=200)
    fase = models.CharField(max_length=30, choices=TIPO_DE_FASE, blank=True)
    resultado = models.CharField(max_length=200, default='Esperando o jogo')
    estadio = models.ForeignKey('Estadio', on_delete=models.CASCADE)
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_do_jogo = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.time_1} X {self.time_2}'
