# ...................................... FRONT PAGE ......................................................

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Photo, Video

def home(request):
    return render(request, 'portfolio/home.html')

def portfolio(request):
    photos = Photo.objects.all()
    videos = Video.objects.all()
    return render(request, 'portfolio/portfolio.html', {'photos': photos, 'videos': videos})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Save the contact details
        Contact.objects.create(name=name, email=email, message=message)
    return render(request, 'portfolio/contact.html')


# ...................................... BOOKING APPOINTMENTS ......................................................

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('view_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'portfolio/book_appointment.html', {'form': form})

@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'portfolio/view_appointments.html', {'appointments': appointments})


# ...................................... LOGIN LOGOUT ......................................................

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import View

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Or redirect to the desired page
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})

    
from django.urls import reverse_lazy
from django.views import View

class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home or any other page after signup
        return render(request, 'registration/signup.html', {'form': form})