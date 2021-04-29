from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'step'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('dasboard/', views.dasboard, name='dasboard'),
    path('entidades/', views.entidades, name='entidades'),
    path('entidades/add/', views.addentidades, name='addEntidades'),
    path('projectos/', views.projectos, name='projectos'),
    path('projecto/add/', views.addprojectos, name='addprojecto'),
    path('login/', auth_views.LoginView.as_view(template_name='step/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

