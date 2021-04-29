from django.shortcuts import redirect, render
import json

def addCategoria(request):
    # print(request.POST['nome'])
    response = json.dumps({"success":True, "msg": 'Categoria adicionada com Sucesso'})
    return response