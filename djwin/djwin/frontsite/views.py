from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from shop.models import *

def home(request):
    return render(request, 'frontsite/home.html')

def singleroom(request, pk_test):
    room = Room.objects.get(id=pk_test)
    context = {'room':room}
    return render(request, 'frontsite/rooms-single.html',context)

def rooms(request):
    
    rooms = Room.objects.all()
    return render(request, 'frontsite/rooms.html',{'rooms':rooms})


