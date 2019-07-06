from django.urls import path
from . import views
from django.conf.urls import url
from .views import home, get_data, ChartData

urlpatterns = [
    path('', views.home, name='charts-home'),
    path('about', views.about, name='charts-about'),
    url(r'^$', home),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
]




