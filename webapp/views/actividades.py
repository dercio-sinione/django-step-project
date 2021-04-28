from django.shortcuts import render, get_object_or_404
from webapp.models import Servicos, Slides, Actividades, Areas


def actividades(request):
    context = {
        'actividadesSubtitulo': Areas.objects.filter(nome='Actividades').first().subtitulo,
        'servicos': Servicos.objects.order_by('nome').all(),
        'slides': Slides.objects.order_by('-dataCriacao').filter(area__nome='Actividades')[:3],
        'actividades': Actividades.objects.order_by('-dataCriacao').all()[:10],
    }
    return render(request, 'webapp/actividades.html', context)

def actividadesDetails(request, pk):
    obj = get_object_or_404(Actividades, pk=pk)
    context = {
        'actividadesSubtitulo': Areas.objects.filter(nome='Actividades').first().subtitulo,
        'servicos': Servicos.objects.order_by('nome').all(),
        'slides': Slides.objects.order_by('-dataCriacao').filter(area__nome='Actividades')[:3],
        'actividades': Actividades.objects.order_by('-dataCriacao').all()[:10],
        'actividadesFull': obj,
    }
    return render(request, 'webapp/actividades-details.html', context)
