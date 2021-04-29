from django.shortcuts import render


def entidades(request):
    return render(request, 'step/entidades.html',)
