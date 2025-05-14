class ServicioElegido:
    def __init__(self, id, customer_id, servicio_nombre, precio, fecha=None):
        self.id = id
        self.customer_id = customer_id
        self.servicio_nombre = servicio_nombre
        self.precio = precio
        self.fecha = fecha
