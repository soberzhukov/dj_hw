from django.http import Http404
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    req = request.GET.get('sort')
    ph = Phone.objects.all()
    if req:
        if req == 'name':
            ph = Phone.objects.order_by('name')
        if req == 'min_price':
            ph = Phone.objects.order_by('price')
        if req == 'max_price':
            ph = Phone.objects.order_by('-price')
    context = {'phones': ph}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    ph = Phone.objects.filter(slug=slug)
    if not ph:
        raise Http404('Такой модели нет')
    context = {
        'phone': ph[0]
    }
    return render(request, template, context)
