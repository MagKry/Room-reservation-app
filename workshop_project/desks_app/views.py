from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

from .models import Room, Reservation


# Create your views here.

def home(request):
    return render(request, "home.html")

def all_rooms(request):
    rooms = Room.objects.all()
    if not rooms:
        return HttpResponse("There are no rooms available.")
    else:
        return render(request, "all_rooms.html", {"rooms": rooms})


def new_room(request):
    if request.method == "GET":
        return render(request, "add_room.html")
    elif request.method == "POST":
        room_name = str(request.POST.get("room_name"))
        room_size = int(request.POST.get("room_size"))
        projector = request.POST.get("projector")
        if projector == 'on':
            projector = True
        else:
            projector = False

        try:
            rooms = Room.objects.all()
            room = Room.objects.create(room_name=room_name, room_size=room_size, projector=projector)
        except IntegrityError:
            return HttpResponse("Error! This room already exists.")

        if room_name == "" :
            return HttpResponse("Error! Room name cannot be blank.")
        elif not isinstance(room_size, int):
            return HttpResponse("Error!Room size must be a number.")
        elif room_size < 0:
            return HttpResponse("Error!Room size must be a positive number.")
        else:
            return render(request, "all_rooms.html", {"rooms": rooms})

def room_details(request, id):
    return render(request, "room_details.html")

def modify_room(request, id):
    if request.method == "GET":
        room = Room.objects.get(id=id)
        return render(request, "modify.html")
    elif request.method == "POST":
        new_room_name = str(request.POST.get("room_name"))
        new_room_size = int(request.POST.get("room_size"))
        new_projector = request.POST.get("projector")
        if new_projector == "on":
            new_projector = True
        else:
            new_projector = False

        new_room = Room.objects.filter(~Q(id=id), room_name=new_room_name, room_size=new_room_size, projector=new_projector).first()
        if new_room:
            return HttpResponse("Error! This room already exists.")

        try:
            Room.objects.filter(id=id).update(room_name=new_room_name, room_size=new_room_size, projector=new_projector)
        except IntegrityError:
            return HttpResponse("Error! This room already exists.")

        if new_room_name == "":
            return HttpResponse("Error! Room name cannot be blank.")
        elif not isinstance(new_room_size, int):
            return HttpResponse("Error!Room size must be a number.")
        elif new_room_size < 0:
            return HttpResponse("Error!Room size must be a positive number.")
        else:
            new_room = Room.objects.filter(id=id).update(room_name=new_room_name, room_size=new_room_size, projector=new_projector)
            rooms = Room.objects.all()
            return render(request, "all_rooms.html", {"rooms": rooms})


def delete_room(request, id):
    if request.method == "GET":
        room = Room.objects.get(id=id)
        room.delete()
        rooms = Room.objects.all()
        return render(request, "delete.html", {"rooms": rooms})

def reserve_room(request, room_id):
    if request.method == "GET":
        room = Room.objects.get(id=room_id)
        return render(request, "reserve.html", {"room": room})
    elif request.method == "POST":
        room = Room.objects.get(id=room_id)
        date = request.POST.get("date")
        comment = request.POST.get("comment")

        if Reservation.objects.filter(room_id=room_id, date=date):
            return render(request, "reserve.html", {"room": room, "Error!": "This room is already booked."})
        if date < datetime.today():
            return render(request, "reserve.html", {"room": room, "Error!": "The date is in the past."})

        Reservation.objects.create(room_id=room_id, date=date, comment=comment)

        return redirect("all_rooms")

