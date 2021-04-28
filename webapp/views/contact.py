from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms

from webapp.models import Endereco, Mensagens, Servicos


class FormMensagens(forms.ModelForm):
    class Meta:
        model = Mensagens
        fields = ['nome', 'email', 'numeroTelefone', 'interesse', 'assunto', 'mensagem']


def contact(request):
    if Endereco.objects.count() == 0:
        obj = Endereco(
            localizacao='Localização da organização',
            email='org@gmail.com',
            tel1='+244 999000000',
            tel2='+244 929000000',
        )
        obj.save()

    if request.method == 'POST':
        form = FormMensagens(request.POST,)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Mensagem enviada com sucesso!')
            return redirect('webapp:contact')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormMensagens()

    context = {
        'endereco': Endereco.objects.first(),
        'servicos': Servicos.objects.all(),
        'form': form,
    }
    return render(request, 'webapp/contact.html', context)
