from django.shortcuts import render, get_object_or_404
from .models import Hoteis
from django.utils import timezone

def hoteis(request):
	posts = Hoteis.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'hoteis/hoteis.html', {'posts': posts})
# Create your views here.


def post_detail(request, pk):
    post = get_object_or_404(Hoteis, pk=pk)
    Hoteis.objects.get(pk=pk)
    return render(request, 'hoteis/post_detail.html', {'post': post})
