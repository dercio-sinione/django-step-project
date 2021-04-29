from django.shortcuts import redirect, render


def addCategoria(request):
    print(request.GET)
    print(request.POST)
    return redirect('step:addprojecto')