from domain.Huesped import Huesped
from domain.Habitacion import Habitacion

class Reserva:

    def __init__(self, id, huesped: Huesped, habitacion: Habitacion, fecha_entrada, fecha_salida):
        self.id = id
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida