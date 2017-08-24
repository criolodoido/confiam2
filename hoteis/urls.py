from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hoteis, name='hoteis'),

]