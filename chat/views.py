from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Room

# Create your views here.
def home(request):
    return render(request, 'homeStuff.html')

def checkForRoom(request):
    room = request.POST['roomName']
    user = request.POST['user']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?user=' + user)
    else:
        newRoom = Room.objects.create(name=room)
        newRoom.save()
        return redirect('/' + room + '/?user=' + user)
        
def room(request, room):
    return HttpResponse('hello')