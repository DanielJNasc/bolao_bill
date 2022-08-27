from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Jogo, Estadio, Time

admin.site.register(Jogo)

admin.site.register(Estadio)

admin.site.register(Time)