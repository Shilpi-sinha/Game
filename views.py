from django.shortcuts import render
from .models import Game


def index(request):
    na = request.POST.get('name1')
    return render(request, 'home.html')


def quest(request):
    c1 = request.POST.get('answer1')
    return render(request, 'result.html')


def quest2(request):
    c2 = request.POST.get('choice1')
    return render(request, 'result2.html')


def summ(request):
    return render(request, 'summary.html')
