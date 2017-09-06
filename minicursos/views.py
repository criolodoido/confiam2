from django.shortcuts import render, get_object_or_404
from .models import Minicursos
from django.utils import timezone

def minicursos(request):
	posts = Minicursos.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'minicursos/minicursos.html', {'posts': posts})
# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Minicursos, pk=pk)
    Minicursos.objects.get(pk=pk)
    return render(request, 'minicursos/post_detail.html', {'post': post})