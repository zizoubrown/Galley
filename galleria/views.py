from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', locals())

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'image-description/search.html',{"message":message,"images": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'image-description/search.html',{"message":message})