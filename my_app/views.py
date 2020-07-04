from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name':'jubin nautiyal'})


def resume(request):
    return render(request, 'resume.html', {'name':'jubin'})


def contact(request):
    return render(request, 'contact.html')