from django.shortcuts import render
from django.utils import timezone

def minicursos(request):
	return render(request, 'minicursos/minicursos.html')
# Create your views here.
