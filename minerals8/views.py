from django.shortcuts import render, get_object_or_404

from .models import Mineral

# Create your views here.


def mineral_list(request):
    """renders template to list html from browser response"""
    minerals = Mineral.objects.all()
    alphabet = Mineral.objects.all().order_by('name')
    return render(request, 'minerals8/list.html', {'minerals':minerals, 'alphabet': alphabet})

def mineral_detail(request, pk):
    """renders template to list html from browser response"""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals8/detail.html', {'mineral':mineral})

def mineral_search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    alphabet = Mineral.objects.all().order_by('name')
    return render(request, 'minerals8/list.html', {'minerals':minerals, 'alphabet': alphabet})

def alphabet_list(request, letter):
    """renders template to list html from browser response"""
    minerals = Mineral.objects.filter(name__istartswith=letter)
    alphabet = Mineral.objects.all().order_by('name')
    return render(request, 'minerals8/list.html', {'minerals':minerals, 'alphabet': alphabet})

def category_list(request, group):
    """renders template to list html from browser response"""
    minerals = Mineral.objects.filter(group__icontains=group)
    alphabet = Mineral.objects.all().order_by('name')
    return render(request, 'minerals8/list.html', {'minerals':minerals, 'alphabet': alphabet})
