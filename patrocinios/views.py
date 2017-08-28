from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Patrocinios

def patrocinios(request):
	patrocinios = Patrocinios.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'patrocinios/patrocinios.html', {'patrocinios': patrocinios})

def post_detail(request, pk):
    patrocinio = get_object_or_404(Patrocinios, pk=pk)
    Patrocinios.objects.get(pk=pk)
    return render(request, 'patrocinios/post_detail.html', {'patrocinio': patrocinio})
# Create your views here.
