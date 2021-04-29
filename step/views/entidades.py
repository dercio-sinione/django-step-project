from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def entidades(request):
    return render(request, 'step/entidades.html',)
