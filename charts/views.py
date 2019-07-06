from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from .models import Play
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

def home(request):
    return render(request, 'charts/home.html')

def about(request):
    return render(request,'charts/about.html')

def get_data(request):
    data ={
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)



class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        labels = ['Users', 'Blue', 'Yellow', 'Green']

        #getting data from db and making it to a list
        num = Play.objects.all().values_list('name', flat=True)


        data = {
            "labels": labels,
            "default": num,
        }

        return Response(data)








