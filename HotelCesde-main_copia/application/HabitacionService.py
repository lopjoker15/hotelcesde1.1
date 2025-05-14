from domain.Habitacion import Habitacion
from data.HabitacionRepository import HabitacionRepository

class HabitacionService:
    def __init__(self):
        self.repo = HabitacionRepository()

    def agregar_habitacion(self, db):
        print("\n--- Agregar Habitación ---")
        numero = input("Número de habitación: ")
        tipo = input("Tipo (Individual, Doble, Suite): ").capitalize()
        precio = float(input("Precio por noche: "))
        estado = input("Estado (Disponible, Ocupada, Mantenimiento): ").capitalize()

        habitacion = Habitacion(None, numero, tipo, precio, estado)
        self.repo.crear_habitacion(db, habitacion)
        print("Habitación agregada con éxito.")

    def listar_habitaciones(self, db):
        print("\n--- Lista de Habitaciones ---")
        habitaciones = self.repo.obtener_todas(db)
        if habitaciones:
            for hab in habitaciones:
                print(f"ID: {hab[0]} | Número: {hab[1]} | Tipo: {hab[2]} | Precio: {hab[3]} | Estado: {hab[4]}")
        else:
            print("No hay habitaciones registradas.")
