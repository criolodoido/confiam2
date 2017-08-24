from django.shortcuts import render
from django.utils import timezone

def palestras(request):
	return render(request, 'palestras/palestras.html')
# Create your views here.
