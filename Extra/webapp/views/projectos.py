from django.shortcuts import render, get_object_or_404
from webapp.models import Areas, Servicos, Slides, Projectos


def projectos(request):
    context = {
        'projectoSubtitulo': Areas.objects.filter(nome='Projectos').first().subtitulo,
        'slides': Slides.objects.order_by('-dataCriacao').filter(area__nome='Projectos')[:3],
        'projectos': Projectos.objects.order_by('-dataCriacao').all()
    }

    return render(request, 'webapp/projectos.html', context)


def projectoDetails(request, pk):
    obj = get_object_or_404(Projectos, pk=pk)
    context = {
        'projectoSubtitulo': Areas.objects.filter(nome='Projectos').first().subtitulo,
        'servicos': Servicos.objects.order_by('nome').all(),
        'slides': Slides.objects.order_by('-dataCriacao').filter(area__nome='Projectos')[:3],
        'projectos': Projectos.objects.order_by('-dataCriacao').all(),
        'projectoFulls': obj,
    }

    return render(request, 'webapp/projecto-details.html', context)
