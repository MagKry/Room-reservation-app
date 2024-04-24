# Room-reservation-app

This is a web application created with use of Django framework. Application provides funtionalities for conference room booking.

Home page:
- lists all rooms with their status on the current day
- each room on the list has the link to modification and deletion 

Room details:
After clicking on the name of the room, user can view the room details:
    name,
    capacity,
    info, if there is projector in the room.

Additionally, user can view the list of days, when the room is booked (only the future ones).
There are also links to:
    room booking form,
    delete the room,
    modify the room.

Adding new room:
  form to adding a room
  
Modifying the room:
After entering the page of room editing, user can provide the details (name, capacity, projector)

Room booking:
After entering the page of room booking, user can view the list of days that the room will be unavailable (the days in the past are exluded). User can provide the date of the reservation, the room cannot be booked for the date already 'taken'. Trying to add another booking will result in the error message. User cannot choose the past date.

Room search:
user can search for the room based on the following criteria:
    name,
    capacity,
    info, if there is projector in the room.
