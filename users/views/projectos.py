from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from webapp.models import Projectos
from users.forms import FormProjecto


# TODO TAREFAS:
# ADICIONAR PAGINAÇÃO
# ADICIONAR PESQUISA DE PROJECTO
# ADICIONAR DETALHES DE UM DETERMINADO PROJECTO

@login_required
def addProjecto(request):
    if request.method == 'POST':
        # Formulario de registar Projectos
        form = FormProjecto(
            request.POST, request.FILES,)
        form.instance.criadoPor = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data.get('titulo')
            messages.success(
                request, f'Projecto "{titulo}" criado com sucesso!')
            return redirect('users:listarprojectos')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormProjecto()
    return render(request, 'users/addProjecto.html', {'form': form})


@login_required
def changeProjecto(request, pk):
    obj = get_object_or_404(Projectos, pk=pk)
    if request.method == 'POST':
        form = FormProjecto(request.POST, request.FILES, instance=obj)
        form.instance.criadoPor = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data.get('titulo')

            messages.success(
                request, f'Projecto "{titulo}" alterado com sucesso!')
            return redirect('users:listarprojectos')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormProjecto(instance=obj)
    return render(request, 'users/editarProjecto.html', {'form': form})


@login_required
def listProjectos(request):
    context = {
        "projectos": Projectos.objects.all(),
    }
    return render(request, 'users/listProjectos.html', context)


@login_required
def deleteProjecto(request, pk):
    obj = get_object_or_404(Projectos, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Projecto "{obj.titulo}" eliminada com sucesso!')
    return redirect('users:listarprojectos')
