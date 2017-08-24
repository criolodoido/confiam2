from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^programacao/', include('programacao.urls', namespace='programacao')),
    url(r'^palestras/', include('palestras.urls', namespace='palestras')),
    url(r'^minicursos/', include('minicursos.urls', namespace='minicursos')),
    url(r'^restaurantes/', include('restaurantes.urls', namespace='restaurantes')),
    url(r'^patrocinios/', include('patrocinios.urls', namespace='patrocinios')),
    url(r'^hoteis/', include('hoteis.urls', namespace='hoteis')),
]
