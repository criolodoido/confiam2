from django.shortcuts import render
from django.utils import timezone

def restaurantes(request):
	return render(request, 'restaurantes/restaurantes.html')
# Create your views here.
