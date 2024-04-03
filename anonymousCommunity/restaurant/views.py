from django.shortcuts import render, get_object_or_404
from .models import Restaurant
# Create your views here.

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {"restaurants": restaurants})

def typicalPost(request, id):
    restaurant = get_object_or_404(Restaurant, pk = id)
    total= Restaurant.objects.count()
    return render(request, 'typicalPost.html', {"restaurant": restaurant, "total": total})