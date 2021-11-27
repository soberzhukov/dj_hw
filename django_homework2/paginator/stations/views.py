from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv

with open(settings.BUS_STATION_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    result = [x for x in reader]



def index(request):
    return redirect(reverse('bus_stations'))

all_articles = [i for i in range(1, 1000)]

def bus_stations(request):
    current_page = request.GET.get('page', '1')
    if not current_page.isnumeric():
        current_page = 1
    paginator = Paginator(result, 10)
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
