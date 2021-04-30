from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from step.models import Notificacoes, Projectos

@login_required
def dasboard(request):
    # idUser = current_user.id
    # pr_parados = Projectos.query.filter_by(idUsuario=idUser,estado="parado").count()
    # pr_producao = Projectos.query.filter_by(idUsuario=idUser,estado="em produção").count()
    # pr_concluido = Projectos.query.filter_by(idUsuario=idUser,estado="concluído").count()
    # pr_total = Projectos.query.filter_by(idUsuario=idUser).count()
    # gr_Projectos = {'total': pr_total,'parados': pr_parados, 'producao': pr_producao, 'concluidos': pr_concluido}

    # alert = Notificacoes.query.filter_by(idUser=current_user.id).all()

    context = {
        'total': Projectos.objects.filter(user=request.user).count(),
        'parados': Projectos.objects.filter(user=request.user, estado='Parado').count(),
        'producao': Projectos.objects.filter(user=request.user, estado='Em produção').count(),
        'concluidos': Projectos.objects.filter(user=request.user, estado='Concluído').count(),
        'alert': Notificacoes.objects.all()[:4],
    }
    return render(request, 'step/dasboard.html', context)
