from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.patrocinios, name='patrocinios'),
	url(r'^patrocinios/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhepatrocinios'),

]