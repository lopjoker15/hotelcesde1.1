from domain.Habitacion import Habitacion

class HabitacionRepository:
    def crear_habitacion(self, db, habitacion):
        query = "INSERT INTO habitacion (numero, tipo, precio, estado) VALUES (%s, %s, %s, %s)"
        values = (habitacion.numero, habitacion.tipo, habitacion.precio, habitacion.estado)
        db.execute_query(query, values)

    def obtener_todas(self, db):
        query = "SELECT * FROM habitacion"
        return db.execute_query(query)
