from django.shortcuts import render, HttpResponse
from .models import Usuario
# Create your views here.


def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        print(novo_usuario.nome)
        print(novo_usuario.idade)
        novo_usuario.save()
        #
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
