from domain.ServicioElegido import ServicioElegido

class ServicioElegidoRepository:
    def guardar_servicio_elegido(self, db, servicio_elegido):
        query = "INSERT INTO servicios_elegidos (customer_id, servicio_nombre, precio) VALUES (%s, %s, %s)"
        values = (servicio_elegido.customer_id, servicio_elegido.servicio_nombre, servicio_elegido.precio)
        db.execute_query(query, values)

