from django.shortcuts import render
from django.utils import timezone
from .models import Restaurantes
from django.shortcuts import render, get_object_or_404

def restaurantes(request):
	restaurantes = Restaurantes.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'restaurantes/restaurantes.html', {'restaurantes': restaurantes})
# Create your views here.

def post_detail(request, pk):
    restaurante = get_object_or_404(Restaurantes, pk=pk)
    Restaurantes.objects.get(pk=pk)
    return render(request, 'restaurantes/post_detail.html', {'restaurante': restaurante})