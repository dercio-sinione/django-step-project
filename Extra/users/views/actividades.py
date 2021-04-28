from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from webapp.models import Actividades, ActividadesLink
from users.forms import FormActividade


# TODO TAREFAS:
# ADICIONAR PAGINAÇÃO
# ADICIONAR PESQUISA DE ACTIVIDADES
# ADICIONAR DETALHES DE UMA DETERMINADA ACTIVIDADE

@login_required
def addActividade(request):
    if request.method == 'POST':
        # Formulario de registar Actividades
        form = FormActividade(
            request.POST, request.FILES,)
        form.instance.criadoPor = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data.get('titulo')
            messages.success(
                request, f'Actividade "{titulo}" criada com sucesso!')
            return redirect('users:listaractividades')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormActividade()
    return render(request, 'users/addActividade.html', {'form': form})


@login_required
def changeActividade(request, pk):
    obj = get_object_or_404(Actividades, pk=pk)
    if request.method == 'POST':
        form = FormActividade(request.POST, request.FILES, instance=obj)
        form.instance.criadoPor = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data.get('titulo')

            messages.success(
                request, f'Actividade "{titulo}" alterada com sucesso!')
            return redirect('users:listaractividades')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormActividade(instance=obj)
    return render(request, 'users/editarActividade.html', {'form': form})


@login_required
def listActividades(request):
    context = {
        "actividades": Actividades.objects.all(),
    }
    return render(request, 'users/listActividades.html', context)


@login_required
def deleteActividade(request, pk):
    obj = get_object_or_404(Actividades, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Actividade "{obj.titulo}" eliminada com sucesso!')
    return redirect('users:listaractividades')


@login_required
def addLink(request, pk):
    actividade = get_object_or_404(Actividades, pk=pk)
    if request.method == 'POST':
        obj = ActividadesLink()
        obj.link = request.POST['link']
        obj.actividade = actividade
        obj.save()
        messages.success(request, f'Link da actividade "{obj.actividade.titulo}" foi adicionado com sucesso!')
        return redirect('users:listaractividades')
    return render(request, 'users/addActividadeLink.html', {'actividade': actividade.titulo})


@login_required
def listActividadeLink(request, pk):
    context = {
        "actividade": get_object_or_404(Actividades, pk=pk),
    }
    return render(request, 'users/listActividadeLinks.html', context)


@login_required
def deleteActividadeLink(request, pk):
    obj = get_object_or_404(ActividadesLink, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Link "{obj.link}" eliminado com sucesso!')
    return redirect('users:actividadeLinks', pk=obj.actividade.pk)
