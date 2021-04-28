from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from webapp.models import Mensagens

@login_required
def listMensagens(request):
    context = {
        "mensagens": Mensagens.objects.all(),
    }
    return render(request, 'users/listMensagens.html', context)


@login_required
def mensagemDetail(request, pk):
    mensagem = get_object_or_404(Mensagens, pk=pk)
    mensagem.lida = True
    mensagem.save()
    return render(request, 'users/mensagemDetail.html', {'mensagen': mensagem})


@login_required
def deleteMensagem(request, pk):
    obj = get_object_or_404(Mensagens, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Mensagem de "{obj.nome}" eliminada com sucesso!')
    return redirect('users:mensagens')
