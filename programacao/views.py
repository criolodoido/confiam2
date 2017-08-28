from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Programacao

def programacao(request):
	programas = Programacao.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'programacao/programacao.html', {'programas': programas})

def post_detail(request, pk):
    programa = get_object_or_404(Programacao, pk=pk)
    Programacao.objects.get(pk=pk)
    return render(request, 'programacao/post_detail.html', {'programa': programa})

# Create your views here.
