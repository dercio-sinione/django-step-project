from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def projectos(request):
    return render(request, 'step/projectos.html',)
