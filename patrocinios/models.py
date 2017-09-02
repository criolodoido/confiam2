# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Patrocinios(models.Model):
	nome = models.CharField(max_length=200, null=False, blank=False)
	apresentacao = models.TextField(null=False, blank=False)
	foto = CloudinaryField('foto', null=True, blank=True)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		#return reverse("detalhe", kwargs={"pk": self.pk})
		return "/patrocinios/%s" %(self.pk)
