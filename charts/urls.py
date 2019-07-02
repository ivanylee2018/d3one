from django.urls import path
from . import views
from django.conf.urls import url
from .views import home, play_count_by_month

urlpatterns = [
    path('', views.home, name='charts-home'),
    path('about', views.about, name='charts-about'),
    url(r'^$', home),
    url(r'^api/play_count_by_month', play_count_by_month, name='play_count_by_month'),
]




