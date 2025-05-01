class User: 
    def __init__(self, id, name, last_name, email, password, status):
        self._id = id
        self._name = name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status


class Room:
    def __init__(self, room_number, room_type, price, is_available=True):
        self.room_number = room_number
        self.room_type = room_type  # Ej: 'individual', 'doble', 'suite'
        self.price = price
        self.is_available = is_available

    def __str__(self):
        return f"Habitación {self.room_number} ({self.room_type}) - ${self.price} - {'Disponible' if self.is_available else 'Ocupada'}"


class Reservation:
    def __init__(self, reservation_id, user: User, room: Room):
        self.reservation_id = reservation_id
        self.user = user
        self.room = room

    def confirm(self):
        if self.room.is_available:
            self.room.is_available = False
            print(f"Reserva confirmada para {self.user.name} {self.user.last_name} en habitación {self.room.room_number}")
        else:
            print("La habitación ya está ocupada.")


if __name__ == "__main__":

    user1 = User(1, "Carlos", "Gómez", "carlos@example.com", "1234", "activo")

   
    room1 = Room(101, "individual", 50.0)
    room2 = Room(102, "doble", 80.0)

   
    print(room1)
    print(room2)

   
    reservation1 = Reservation(1, user1, room1)
    reservation1.confirm()

    print(room1)