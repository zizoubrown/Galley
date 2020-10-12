from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def image(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images':images})

def location(request):
    locations = Location.objects.all()
    return render(request, 'home.html', {'locations':locations})

def category(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories':categories})