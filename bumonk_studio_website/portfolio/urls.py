from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='Video Collection'),
    path('portfolio/', views.portfolio, name='Photograhy Collection'),
    path('contact/', views.contact, name='Book an Appointment'),
]
