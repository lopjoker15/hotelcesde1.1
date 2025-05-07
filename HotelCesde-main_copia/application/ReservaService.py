from domain.Reserva import Reserva
from data.ReservaRepository import ReservaRepository
import datetime

class ReservaService:
    def __init__(self):
        self.repo = ReservaRepository()

    def hacer_reserva(self, db):
        print("\n--- Hacer una Reserva ---")
        nombre = input("Nombre: ")
        fecha_entrada = input("Fecha de entrada (YYYY-MM-DD): ")
        fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")
        tipo_habitacion = input("Tipo de habitación (Individual, Doble, Suite): ").capitalize()

        try:
            entrada = datetime.datetime.strptime(fecha_entrada, "%Y-%m-%d")
            salida = datetime.datetime.strptime(fecha_salida, "%Y-%m-%d")
            if entrada >= salida:
                print("Error: La fecha de salida debe ser después de la de entrada.")
                return
        except ValueError:
            print("Formato de fecha inválido.")
            return

        reserva = Reserva(None, nombre, entrada, salida, tipo_habitacion)
        self.repo.createReserva(db, reserva)
        print("Reserva realizada con éxito.")