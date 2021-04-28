from django.shortcuts import render
from webapp.models import Servicos, Slides, Projectos, Actividades, ActividadesLink, Areas


def index(request):
    # actividadeLink = ActividadesLink.objects.raw('''
    #     select distinct actividade_id as id from webapp_actividadeslink order by actividade_id desc
    # ''')[:3]
    
    totAreas = Areas.objects.count()
    if totAreas == 0:
        data = [
                Areas(nome="Home"), 
                Areas(nome="Actividades"),
                Areas(nome="Projectos"),
                Areas(nome="Serviços"), 
                Areas(nome="Slides")
                ]
        for item in data:
            item.save()
            
    context = {
        'projectoSubtitulo': Areas.objects.filter(nome='Projectos').first().subtitulo,
        'actividadeSubtitulo': Areas.objects.filter(nome='Actividades').first().subtitulo,
        'slides': Slides.objects.order_by('-dataCriacao').filter(area__nome="Home")[:3],
        'projectos': Projectos.objects.order_by('-id').all()[:3],
        'actividades': Actividades.objects.order_by('-id').all()[:3],
        # 'actividadeLink': actividadeLink,
    }
    return render(request, 'webapp/index.html', context)
