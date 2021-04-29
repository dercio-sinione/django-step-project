from django.shortcuts import render
from step.models import Notificacoes


def dasboard(request):
    # idUser = current_user.id
    # pr_parados = Projectos.query.filter_by(idUsuario=idUser,estado="parado").count()
    # pr_producao = Projectos.query.filter_by(idUsuario=idUser,estado="em produção").count()
    # pr_concluido = Projectos.query.filter_by(idUsuario=idUser,estado="concluído").count()
    # pr_total = Projectos.query.filter_by(idUsuario=idUser).count()
    # gr_Projectos = {'total': pr_total,'parados': pr_parados, 'producao': pr_producao, 'concluidos': pr_concluido}

    # alert = Notificacoes.query.filter_by(idUser=current_user.id).all()

    context = {
        'total': 2,
        'parados': 2,
        'producao': 2,
        'concluidos': 2,
        'alert': Notificacoes.objects.all()[:4],
    }
    return render(request, 'step/dasboard.html', context)
