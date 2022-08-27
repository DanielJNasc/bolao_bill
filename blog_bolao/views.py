from django.shortcuts import render
from .models import Jogo

# Create your views here.
def jogo_list(request):
    todos_os_jogos = Jogo.objects.all()
    return render(request, 'blog_bolao/jogo_list.html', {'jogos': todos_os_jogos})

