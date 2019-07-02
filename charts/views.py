from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from .models import Play

def home(request):
    return render(request, 'charts/home.html')

def about(request):
    return render(request,'charts/about.html')

def play_count_by_month(request):
    data = Play.objects.all()\
        .extra(select={'month': connections[Play.objects.db].ops.date_trunc_sql('month', 'date')}) \
        .values('month')\
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)





