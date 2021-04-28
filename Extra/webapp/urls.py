from django.urls import path
from .views import index, servicos, projectos, actividades, contact, projectoDetails, sobre, actividadesDetails


app_name = 'webapp'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('servico/<int:pk>', servicos, name='servicos'),
    path('projectos/', projectos, name='projectos'),
    path('projecto-details/<int:pk>', projectoDetails, name='projecto-details'),
    path('actividades-details/<int:pk>', actividadesDetails, name='actividades-details'),
    path('actividades/', actividades, name='actividades'),
    path('contactos/', contact, name='contact'),
    path('sobre/', sobre, name='sobre')
]

# projecto-details
