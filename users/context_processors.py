
def show_mensagens(request):
    from webapp.models import Mensagens
    mensagens = Mensagens.objects.filter(lida=False).order_by('-dataCriacao')
    return {
        'mensagens_unread': mensagens[:3],
        'totMensagens': mensagens.count() if mensagens.count() > 0 else ''
    }