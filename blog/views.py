from django.shortcuts import render
from django.views.generic.base import View
from .models import News


def home(request):
    data = {'news': News.objects.all(),
            'title': 'Главная страница блога'
            }
    return render(request, 'blog/home.html', context=data)


def contacts(request):
    return render(request, 'blog/contacts.html')
