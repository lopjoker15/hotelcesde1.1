class Pago:
    def __init__(self, id, id_cliente, monto, metodo_pago, fecha):
        self.id = id
        self.id_cliente = id_cliente
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.fecha = fecha
