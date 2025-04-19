from django.urls import path
from . import views

urlpatterns = [
    path('pm25/', views.pm25_lookup_view, name='pm25_lookup'),
    path('pm25/compare/', views.barchart_compare, name='barchart_compare'),
    path('homepage', views.homepage, name='homepage'),
]
