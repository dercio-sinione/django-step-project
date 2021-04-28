from django.contrib import admin
from .models import (Actividades, Areas, Projectos, Servicos,
                     ServicosDetalhes, Slides, Sobre, ActividadesLink, Mensagens)


admin.site.register(Actividades)
admin.site.register(Areas)
admin.site.register(Projectos)
admin.site.register(Servicos)
admin.site.register(ServicosDetalhes)
admin.site.register(Slides)
admin.site.register(Sobre)
admin.site.register(ActividadesLink)
admin.site.register(Mensagens)
