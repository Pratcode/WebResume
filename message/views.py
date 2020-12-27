from django.shortcuts import render, redirect
from .models import Message


# Create your views here.

def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']    #this message is the value which is comming from form.
        msg_save = Message(Message_name=name, Message_email=email, Message_body=msg)
        msg_save.save()
        return redirect('contact')
