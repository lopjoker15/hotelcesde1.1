from domain.Reserva import Reserva

class Pago:
    def __init__(self, id, reserva: Reserva, monto, metodo_pago):
        self.id = id
        self.reserva = reserva
        self.monto = monto
        self.metodo_pago = metodo_pago

    def __str__(self):
        return f"Pago(ID={self.id}, Reserva={self.reserva.id}, Monto={self.monto}, Método={self.metodo_pago})"