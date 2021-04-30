from django.shortcuts import render


def index(request):
    # context = {
    #     'actividades': Actividades.objects.order_by('-id').all()[:3],
    # }
    return render(request, 'step/index.html',)


def registar(request):
    # context = {
    #     'actividades': Actividades.objects.order_by('-id').all()[:3],
    # }
    return render(request, 'step/registar.html',)
