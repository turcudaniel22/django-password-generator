from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "Generator/home.html")


def about(request):
    return render(request, "Generator/about.html")

def password(request):

    characaters = list('abcdefghijmniqrstwxiz')

    if request.GET.get('uppercase'):
        characaters.extend(list('ABCDEFGHIJMNIQRSTWXIZ'))
    if request.GET.get('characters'):
        characaters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        characaters.extend(list('123456789'))

    length = int(request.GET.get('length', 8))

    length = 10

    thepassword  = ''
    for x in range(length):
        thepassword += random.choice(characaters)

    return render(request, "Generator/password.html",{'password':thepassword})