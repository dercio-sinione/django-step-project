from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms

from step.models import Entidades


class FormEntidade(forms.ModelForm):
    class Meta:
        model = Entidades
        fields = ['nome', 'email', 'contacto',]


@login_required
def entidades(request):
    context = {
        "result": Entidades.objects.filter(user=request.user),
        }
    return render(request, 'step/entidades.html', context)


@login_required
def addentidades(request):
    
    print(request.POST)
    if request.method == 'POST':
        form = FormEntidade(request.POST,)
        form.instance.user = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('nome')
            messages.success(
                request, f'Entidade "{nome}" criado com sucesso!')
            return redirect('step:entidades')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormEntidade()
    return render(request, 'step/entidades.html', {'form': form})

@login_required
def editarentidades(request, pk):
    obj = get_object_or_404(Entidades, pk=pk)
    print(request.POST)
    if request.method == 'POST':
        form = FormEntidade(request.POST, instance=obj)
        form.instance.user = request.user

        # Validar o formulario
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('nome')
            messages.success(
                request, f'Entidade "{nome}" editada com sucesso!')
            return redirect('step:entidades')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormEntidade(instance=obj)
    return render(request, 'step/entidades.html', {'form': form})


@login_required
def deleteEntidade(request, pk):
    obj = get_object_or_404(Entidades, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Entidade "{obj.nome}" eliminada com sucesso!')
    return redirect('step:entidades')
