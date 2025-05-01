from domain.Habitacion import Habitacion
from domain.Employee import Employee

class Servicio:
    def __init__(self, id, habitacion: Habitacion, empleado: Employee, descripcion):
        self.id = id
        self.habitacion = habitacion
        self.empleado = empleado
        self.descripcion = descripcion

    def __str__(self):
        return f"Servicio(ID={self.id}, Habitación={self.habitacion.numero}, Empleado={self.empleado.name}, " \
               f"Descripción={self.descripcion})"