from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib import messages
from register.models import *


# Create your views here.

def home(request):
    return render(request, 'log.html')

# def ind(request):
#     return render(request, 'index.html')

def T_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        city = request.POST['city']
        password = request.POST['password']
        try:
            registration(name=name, email=email, password=password, phonenumber=phonenumber,
                                 city=city).save()
            return redirect('/Task_register/')
        except IntegrityError as e:
            messages.info(request, "name already exists")
            return redirect('/Task_register/ ')
    return render(request, 'log.html')

def home2(request):
    return render(request, 'html1.html')
def T_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            r = registration.objects.get(email=email, password=password)
            request.session['user'] = email
            X = str(r.name)
            y = X.capitalize()
            message_content = f"{y}, you have been Log-In"
            messages.info(request, message_content)
            return redirect('/login/')
        except:
            message_content = "Wrong Password"
            messages.info(request, message_content)
    return render(request, 'log.html')