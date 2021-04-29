from django.shortcuts import redirect, render
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
        "result": Entidades.objects.all(),
        }
    return render(request, 'step/entidades.html', context)


@login_required
def addentidades(request):
    if request.method == 'POST':
        form = FormEntidade()
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
