from django.shortcuts import render, get_object_or_404
from .models import HelpCenter

# Create your views here.


def index(request):
    help_centers = HelpCenter.objects.all()
    context = {
        'help_centers': help_centers,
    }
    return render(request, 'connect/index.html', context)


def center(request, pk):
    center = get_object_or_404(HelpCenter, pk=pk)
    help_center = HelpCenter.objects.filter(pk=pk)
    context = {
        'center': center,
        'help_center': help_center,
    }
    return render(request, 'connect/center.html', context)