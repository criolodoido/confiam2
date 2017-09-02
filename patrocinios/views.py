from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Patrocinios

def patrocinios(request):
	posts = Patrocinios.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'patrocinios/patrocinios.html', {'posts': posts})

def post_detail(request, pk):
    ppost = get_object_or_404(Patrocinios, pk=pk)
    Patrocinios.objects.get(pk=pk)
    return render(request, 'patrocinios/post_detail.html', {'post': post})
# Create your views here.
