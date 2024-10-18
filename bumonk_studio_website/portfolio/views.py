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
