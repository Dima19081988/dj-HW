from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    stations_list = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            stations_list.append({
	            'Name': row.get('Name', '').strip(),
	            'Street': row.get('Street', '').strip(),
	            'District': row.get('District', '').strip()
            })
    paginator = Paginator(stations_list, 10)

    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except Exception:
        page_obj = paginator.page(1)

    context = {
	    'bus_stations': page_obj.object_list,
	    'page': page_obj,
    }

    return render(request, 'stations/index.html', context)
