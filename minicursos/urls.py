from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.minicursos, name='minicursos'),
	url(r'^minicurso/(?P<pk>[0-9]+)/$', views.post_detail, name='detalheminicursos'),
]