from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.programacao, name='programacao'),
	url(r'^programacao/(?P<pk>[0-9]+)/$', views.post_detail, name='detalheprogramacao'),

]