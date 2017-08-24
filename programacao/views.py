from django.shortcuts import render
from django.utils import timezone

def programacao(request):
	return render(request, 'programacao/programacao.html')
# Create your views here.
