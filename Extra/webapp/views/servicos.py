from django.shortcuts import render, get_object_or_404
from webapp.models import Servicos


def servicos(request, pk):
    servico = get_object_or_404(Servicos, pk=pk)
    context = {
        'servico': servico,
    }
    return render(request, 'webapp/servico.html', context)
