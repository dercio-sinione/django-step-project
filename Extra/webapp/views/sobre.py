from django.shortcuts import render, get_object_or_404
from webapp.models import Sobre


def sobre(request):
    context = {
        'sobre': Sobre.objects.all()
    }

    return render(request, 'webapp/sobre.html', context)