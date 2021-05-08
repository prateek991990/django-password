from django.shortcuts import render
import random


# Create your views here.


def home(request):
    return render(request, 'password/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    length = int(request.GET.get('lenght', 12))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('Number'):
        characters.extend(list('0123456789'))

    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password/password.html', {'password': thepassword})


def about(request):
    return render(request, 'password/about.html')
