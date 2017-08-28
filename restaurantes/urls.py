from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.restaurantes, name='restaurantes'),
	url(r'^restaurante/(?P<pk>[0-9]+)/$', views.post_detail, name='detalherestaurante'),

]