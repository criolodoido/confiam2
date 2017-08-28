from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hoteis, name='hoteis'),
	url(r'^hoteis/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhehoteis'),

]