from django.shortcuts import render
from .models import Data
from medapp.models import Media


# Create your views here.


def home(request):
    data_cards = Data.objects.all()
    media_suff = Media.objects.all()
    return render(request, 'home.html', {'data_cards': data_cards, 'media_suff': media_suff})







