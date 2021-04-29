from django.shortcuts import render


def projectos(request):
    return render(request, 'step/projectos.html',)
