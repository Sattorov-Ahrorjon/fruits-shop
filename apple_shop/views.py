from django.shortcuts import render
from .models import Fruit
from random import choice


def get_main_page(request):
    fruit_list = Fruit.objects.all()[:3]
    context = {
        'fruit_list': fruit_list,
        'fruit_one': choice(fruit_list),
    }
    return render(request, 'index.html', context=context)
