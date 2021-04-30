from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'step'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('registar/', views.registar, name='registar'),
    path('dasboard/', views.dasboard, name='dasboard'),
    path('entidades/', views.entidades, name='entidades'),
    path('entidades/add/', views.addentidades, name='addEntidades'),
    path('entidade/<int:pk>/editar/', views.editarentidades, name='editarEntidades'),
    path('entidade/<int:pk>/eliminar/', views.deleteEntidade, name='eliminarEntidade'),
    path('projectos/', views.projectos, name='projectos'),
    path('projecto/add/', views.addProjecto, name='addprojecto'),
    path('projecto/<int:pk>/editar/', views.editarProjecto, name='editarProjecto'),
    path('projecto/<int:pk>/eliminar/', views.deleteProjecto, name='eliminarProjecto'),
   
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/add/', views.addCategoria, name='addCategoria'),
    path('categoria/<int:pk>/editar/', views.editarCategoria, name='editarCategoria'),
    path('categoria/<int:pk>/eliminar/', views.deleteCategoria, name='eliminarCategoria'),
    
    path('login/', auth_views.LoginView.as_view(template_name='step/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

