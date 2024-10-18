from django.urls import path
from . import views 
from .views import SignUpView

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='Video Collection'),
    path('portfolio/', views.portfolio, name='Photograhy Collection'),
    path('contact/', views.contact, name='Book an Appointment'),

    path('book/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.view_appointments, name='view_appointments'),
    path('login/', views.custom_login, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]