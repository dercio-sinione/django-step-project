from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages

from webapp.models import Servicos, Slides
from users.forms import FormSlide

@login_required
def addSlide(request):
    if request.method == 'POST':
        form = FormSlide(request.POST, request.FILES)
        # form.instance.criadoPor = request.user

        if form.is_valid():
            form.save()

            messages.success(request, f"Slide para área {form.cleaned_data.get('area')} adicionada com sucesso!")
            return redirect('users:listarSlide')
        else:
            messages.error(request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormSlide()
    return render(request, 'users/slide.html', {'form': form})


@login_required
def changeSlide(request, pk):

    obj = get_object_or_404(Slides, pk=pk)

    if request.method == 'POST':
        form = FormSlide(request.POST, instance=obj)

        if form.is_valid():
            form.save()

            messages.success(request, "Slide atualizado com sucesso!")
            return redirect('users:listarSlide')
        else:
            messages.error(
                request, f'{form.errors}', extra_tags='danger')
    else:
        form = FormSlide(instance=obj)
    return render(request, 'users/slide.html', {'form': form})


@login_required
def listSlide(request):
    context = {
        "slides": Slides.objects.order_by('area').all(),
    }
    return render(request, 'users/listSlide.html', context)


@login_required
def deleteSlide(request, pk):
    obj = get_object_or_404(Slides, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Slide eliminado com sucesso!')
    return redirect('users:listarSlide')
