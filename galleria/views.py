from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', locals())
