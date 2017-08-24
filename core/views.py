from django.shortcuts import render
from django.utils import timezone
from .models import Evento
from django.shortcuts import render, get_object_or_404

def index(request):
	posts = Evento.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'core/index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Evento, pk=pk)
    Evento.objects.get(pk=pk)
    return render(request, 'core/post_detail.html', {'post': post})