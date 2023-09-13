from django.shortcuts import render
from .data import fruit_list, hate

# Create your views here.
def fruit(request):
    context = {
        'fruit_list': fruit_list,
        'hate': hate,
    }
    return render(request, 'fruits/fruit.html', context)