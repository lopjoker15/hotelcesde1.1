from domain.User import Room

class RoomRepository:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_available_rooms(self):
        return [room for room in self.rooms if room.is_available]

    def get_room_by_number(self, number):
        for room in self.rooms:
            if room.room_number == number:
                return room
        return None
