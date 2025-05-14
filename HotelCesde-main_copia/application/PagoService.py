from domain.Pagos import Pago
from data.PagoRepository import PagoRepository
import datetime

class PagoService:
    def __init__(self):
        self.repo = PagoRepository()

    def realizar_pago(self, db, id_cliente):
        print("\n--- Realizar Pago ---")
        monto = float(input("Ingrese el monto a pagar: "))
        metodo_pago = input("Método de pago (efectivo, tarjeta, etc.): ").capitalize()
        fecha = datetime.datetime.now()

        pago = Pago(None, id_cliente, monto, metodo_pago, fecha)
        self.repo.create_pago(db, pago)
        print("Pago registrado exitosamente.")
