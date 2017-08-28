from django.shortcuts import render, get_object_or_404
from .models import Palestras
from django.utils import timezone

def palestras(request):
	palestras = Palestras.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'palestras/palestras.html', {'palestras': palestras})


def post_detail(request, pk):
    palestra = get_object_or_404(Palestras, pk=pk)
    Palestras.objects.get(pk=pk)
    return render(request, 'palestras/post_detail.html', {'palestra': palestra})
# Create your views here.
