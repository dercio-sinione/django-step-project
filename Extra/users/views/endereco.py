from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages

from webapp.models import Endereco
from users.forms import FormEndereco


@login_required
def changeEndereco(request):
    if Endereco.objects.count() == 0:
        obj = Endereco(
            localizacao='Localização da organização',
            email='org@gmail.com',
            tel1='+244 999000000',
            tel2='+244 929000000',
            atualizadoPor=request.user
        )
        obj.save()

    obj = Endereco.objects.first()

    if request.method == 'POST':
        form = FormEndereco(request.POST, instance=obj)
        form.instance.criadoPor = request.user

        if form.is_valid():
            form.save()

            messages.success(request, 'Endereço actualizado com sucesso!')
            return redirect('users:endereco')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormEndereco(instance=obj)
    return render(request, 'users/endereco.html', {'form': form})
