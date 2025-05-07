from data.HabitacionRepository import RoomRepository
from domain.User import Room

class RoomService:
    def __init__(self, room_repo: RoomRepository):
        self.room_repo = room_repo

    def create_room(self, room_number, room_type, price):
        room = Room(room_number, room_type, price)
        self.room_repo.add_room(room)
        return room

    def list_available_rooms(self):
        return self.room_repo.get_available_rooms()
