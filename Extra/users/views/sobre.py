from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages

from webapp.models import Sobre
from users.forms import FormSobre

@login_required
def addSobre(request):
    if request.method == 'POST':
        form = FormSobre(request.POST,)
        form.instance.criadoPor = request.user

        if form.is_valid():
            form.save()

            messages.success(request, 'Informação Adicionada com sucesso!')
            return redirect('users:listarSobre')
        else:
            messages.error(request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormSobre()
    return render(request, 'users/sobre.html', {'form': form})


@login_required
def changeSobre(request, pk):

    obj = get_object_or_404(Sobre, pk=pk)

    if request.method == 'POST':
        form = FormSobre(request.POST, instance=obj)
        form.instance.criadoPor = request.user

        if form.is_valid():
            form.save()

            messages.success(request, 'Informação actualizada com sucesso!')
            return redirect('users:listarSobre')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormSobre(instance=obj)
    return render(request, 'users/sobre.html', {'form': form})


@login_required
def listSobre(request):
    context = {
        "all_sobre": Sobre.objects.all(),
    }
    return render(request, 'users/listSobre.html', context)


@login_required
def deleteSobre(request, pk):
    obj = get_object_or_404(Sobre, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(request, f'Serviço "{obj.titulo}" eliminado com sucesso!')
    return redirect('users:listarSobre')
