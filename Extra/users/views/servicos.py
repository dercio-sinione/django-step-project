from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages

from webapp.models import Servicos, ServicosDetalhes


@login_required
def addServico(request):
    try:
        if request.method == 'POST':
            obj = Servicos()
            obj.nome = request.POST['nome']
            obj.titulo = request.POST['titulo']
            obj.conteudo = request.POST['conteudo']
            file = request.FILES.get('imagem', None)
            if file:
                obj.imagem = file
            obj.criadoPor = request.user
            obj.save()
            # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
            messages.success(
                request, f'Serviço "{obj.nome}" criado com sucesso!')
            return redirect('users:listarservicos')
            # IntegrityError
    # O sistema cairá nesta excessão de erro caso tentar apostar mais de uma vez numa partida.
    except IntegrityError:
        # print(f'Erro: {ms.__cause__}')
        messages.error(request, f' Serviço com nome "{obj.nome}" já existe.', extra_tags='danger')
        return redirect('users:addservico')
    return render(request, 'users/addServico.html')


@login_required
def changeServico(request, pk):
    obj = get_object_or_404(Servicos, pk=pk)
    context = {"form": obj, }
    try:
        if request.method == 'POST':
            obj.nome = request.POST['nome']
            obj.titulo = request.POST['titulo']
            obj.conteudo = request.POST['conteudo']
            obj.criadoPor = request.user
            file = request.FILES.get('imagem', None)
            if file:
                obj.imagem = file
            obj.save()

            # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
            messages.success(
                request, f'Serviço "{obj.nome}" editado com sucesso!')
            return redirect('users:listarservicos')
    except IntegrityError:
        # print(f'Erro: {ms.__cause__}')
        messages.error(
            request, f' Serviço com nome "{obj.nome}" já existe.', extra_tags='danger')
        return redirect('users:editar-servico', pk=pk)
    return render(request, 'users/editarServico.html', context)


@login_required
def listServico(request):
    context = {
        "servicos": Servicos.objects.all(),
    }
    return render(request, 'users/listServicos.html', context)


@login_required
def deleteServico(request, pk):
    obj = get_object_or_404(Servicos, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(
        request, f'Serviço "{obj.nome}" eliminado com sucesso!')
    return redirect('users:listarservicos')


@login_required
def addDetalhesServico(request, pk):
    servico = get_object_or_404(Servicos, pk=pk)
    if request.method == 'POST':
        obj = ServicosDetalhes()
        obj.servico = servico
        obj.titulo = request.POST['titulo']
        obj.conteudo = request.POST['conteudo']
        obj.criadoPor = request.user
        obj.save()
        # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
        messages.success(request, f'Detalhe "{obj.titulo}" em "{obj.servico.nome}" criado com sucesso!')
        return redirect('users:listarservicos')
    # O sistema cairá nesta excessão de erro caso tentar apostar mais de uma vez numa partida.
    return render(request, 'users/addDetalhesServico.html', {'servico': servico.nome})


@login_required
def changeServicoDetalhes(request, pk):
    obj = get_object_or_404(ServicosDetalhes, pk=pk)
    context = {
        'servico': obj.servico.nome,
        'form': obj
    }
    if request.method == 'POST':
        obj.titulo = request.POST['titulo']
        obj.conteudo = request.POST['conteudo']
        obj.criadoPor = request.user
        obj.save()
        # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
        messages.success(request, f'Detalhe "{obj.titulo}" em "{obj.servico.nome}" atualizado com sucesso!')
        return redirect('users:listarservicodetalhes', pk=obj.servico.pk)
    # O sistema cairá nesta excessão de erro caso tentar apostar mais de uma vez numa partida.
    return render(request, 'users/addDetalhesServico.html', context)

@login_required
def listServicoDetalhes(request, pk):
    context = {
        "servico": get_object_or_404(Servicos, pk=pk),
    }
    return render(request, 'users/listServicoDetalhes.html', context)

@login_required
def deleteServicoDetalhe(request, pk):
    obj = get_object_or_404(ServicosDetalhes, pk=pk)
    obj.delete()
    # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
    messages.success(request, f'Detalhe "{obj.titulo}" em "{obj.servico.nome}" eliminado com sucesso!')
    return redirect('users:listarservicodetalhes', pk=obj.servico.pk)
