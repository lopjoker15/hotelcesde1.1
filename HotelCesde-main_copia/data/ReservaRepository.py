from domain.Reserva import Reserva

class ReservaRepository:
    def createReserva(self, db, reserva):
        query = "INSERT INTO reservas (nombre, fecha_entrada, fecha_salida, tipo_habitacion) VALUES (%s, %s, %s, %s)"
        values = (reserva.nombre, reserva.fecha_entrada, reserva.fecha_salida, reserva.tipo_habitacion)
        db.execute_query(query, values)
