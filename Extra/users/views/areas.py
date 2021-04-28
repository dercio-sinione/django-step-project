from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages

from webapp.models import Areas


@login_required
def changeArea(request, pk):
    obj = get_object_or_404(Areas, pk=pk)
    context = {
        "form": obj,
    }
    try:
        if request.method == 'POST':
            obj.nome = request.POST['nome']
            obj.subtitulo = request.POST['subtitulo']
            obj.criadoPor = request.user
            obj.save()
            # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
            messages.success(
                request, f'Área "{obj.nome}" actualizada com sucesso!')
            return redirect('users:listarareas')
    except IntegrityError:
        messages.error(
            request, f' Área com nome "{obj.nome}" já existe.', extra_tags='danger')
        return redirect('users:area', pk=pk)
    return render(request, 'users/editarArea.html', context)


@login_required
def listAreas(request):
    # print('*********************')
    # print(Areas.objects.all())
    # print('*********************')
    context = {
        "areas": Areas.objects.all(),
    }
    return render(request, 'users/listAreas.html', context)
