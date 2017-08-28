from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.palestras, name='palestras'),
	url(r'^palestras/(?P<pk>[0-9]+)/$', views.post_detail, name='detalhepalestras'),

]