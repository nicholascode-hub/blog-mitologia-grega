from django.shortcuts import render, get_object_or_404
from .models import Deus

def lista_deuses(request):
    deuses = Deus.objects.all()
    return render(request, 'blog/lista_deuses.html', {'deuses': deuses})

def detalhe_deus(request, deus_id):
    deus = get_object_or_404(Deus, pk=deus_id)
    return render(request, 'blog/detalhe_deus.html', {'deus': deus})

