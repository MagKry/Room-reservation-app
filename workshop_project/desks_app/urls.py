"""
URL configuration for workshop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import home, all_rooms, new_room, room_details, modify_room, delete_room, reserve_room

urlpatterns = [
    path('home/', home, name="home"),
    path('all_rooms/', all_rooms, name="all_rooms"),
    path('new/', new_room, name="new_room"),
    path('room_details/<int:id>/', room_details, name="room_details"),
    path('modify/<int:id>/', modify_room, name="modify_room"),
    path('delete/<int:id>/', delete_room, name="delete_room"),
    path('reserve/<int:room_id>/', reserve_room, name="reserve_room"),

]
