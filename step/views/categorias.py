from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms

from step.models import Categorias


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nome', ]


@login_required
def categorias(request):
    context = {
        "categorias": Categorias.objects.all(),
        }
    return render(request, 'step/categorias.html', context)


@login_required
def addCategoria(request):
    
    print(request.POST)
    if request.method == 'POST':
        form = FormCategoria(request.POST,)
        form.instance.user = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('nome')
            messages.success(
                request, f'Categoria "{nome}" criada com sucesso!')
            return redirect('step:categorias')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormCategoria()
    return render(request, 'step/categorias.html', {'form': form})


@login_required
def editarCategoria(request, pk):
    obj = get_object_or_404(Categorias, pk=pk)
    print(request.POST)
    if request.method == 'POST':
        form = FormCategoria(request.POST, instance=obj)
        form.instance.user = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('nome')
            messages.success(
                request, f'Categoria "{nome}" editada com sucesso!')
            return redirect('step:categorias')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormCategoria(instance=obj)
    return render(request, 'step/categorias.html', {'form': form})


@login_required
def deleteCategoria(request, pk):
    obj = get_object_or_404(Categorias, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Categoria "{obj.nome}" eliminada com sucesso!')
    return redirect('step:categorias')
