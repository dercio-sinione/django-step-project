from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dilide-admin', views.index, name='dilide-admin'),

    path('servicos', views.listServico, name='listarservicos'),
    path('servico/add', views.addServico, name='addservico'),
    path('servico/<int:pk>/adddetalhes', views.addDetalhesServico, name='addservicodetalhes'),
    path('servico/<int:pk>/detalhes', views.listServicoDetalhes, name='listarservicodetalhes'),
    path('servico/<int:pk>/update', views.changeServico, name='editar-servico'),
    path('servicodetalhes/<int:pk>/update', views.changeServicoDetalhes, name='changeServicoDetalhes'),
    path('servico/<int:pk>/delete', views.deleteServico, name='delete-servico'),
    path('servicodetalhe/<int:pk>/delete', views.deleteServicoDetalhe, name='deleteservicodetalhe'),

    path('actividades', views.listActividades, name='listaractividades'),
    path('actividade/add', views.addActividade, name='addactividade'),
    path('actividade/<int:pk>/addlink', views.addLink, name='addactividadeLink'),
    path('actividade/<int:pk>/links', views.listActividadeLink, name='actividadeLinks'),
    path('actividade/<int:pk>/editar', views.changeActividade, name='editar-actividade'),
    path('actividade/<int:pk>/delete', views.deleteActividade, name='delete-actividade'),
    path('link/<int:pk>/delete', views.deleteActividadeLink, name='delete-link'),

    path('projectos', views.listProjectos, name='listarprojectos'),
    path('projecto/add', views.addProjecto, name='addprojecto'),
    path('projecto/<int:pk>/editar', views.changeProjecto, name='editar-projecto'),
    path('projecto/<int:pk>/delete', views.deleteProjecto, name='delete-projecto'),

    path('area/<int:pk>/editar', views.changeArea, name='area'),
    path('areas', views.listAreas, name='listarareas'),

    path('mensagens', views.listMensagens, name='mensagens'),
    path('mensagem/<int:pk>', views.mensagemDetail, name='mensagemDetail'),
    path('mensagem/<int:pk>/delete', views.deleteMensagem, name='deleteMensagem'),

    path('endereco/', views.changeEndereco, name='endereco'),

    path('sobre/all', views.listSobre, name='listarSobre'),
    path('sobre/add', views.addSobre, name='addSobre'),
    path('sobre/<int:pk>/editar', views.changeSobre, name='editarSobre'),
    path('sobre/<int:pk>/delete', views.deleteSobre, name='deleteSobre'),

    path('slides/', views.listSlide, name='listarSlide'),
    path('slide/add', views.addSlide, name='addSlide'),
    path('slide/<int:pk>/editar', views.changeSlide, name='editarSlide'),
    path('slide/<int:pk>/delete', views.deleteSlide, name='deleteSlide'),
]
