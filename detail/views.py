from django.shortcuts import render
from .models import Section, Person


# Create your views here.

def resume(request):
    Person_Details = Person.objects.all()
    return render(request, 'resume.html', {'Person_Details': Person_Details})


def contact(request):
    Person_Details = Person.objects.all()
    return render(request, 'contact.html', {'Person_Details': Person_Details})


def home(request):
    Category_Sections = Section.objects.all()
    Person_Details = Person.objects.all()
    return render(request, 'home.html', {'Category_Sections': Category_Sections, 'Person_Details': Person_Details})







