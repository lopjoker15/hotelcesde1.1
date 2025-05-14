from domain.ServicioElegido import ServicioElegido
from data.ServicioElegidoRepository import ServicioElegidoRepository

class ServicioService:
    def __init__(self):
        self.repo = ServicioElegidoRepository()
        self.servicios_disponibles = [
            {"nombre": "Spa", "precio": 50.00},
            {"nombre": "Desayuno buffet", "precio": 15.00},
            {"nombre": "Piscina", "precio": 20.00}
        ]

    def mostrar_servicios(self, db, customer_id):
        print("\n--- Servicios Disponibles ---")
        for i, servicio in enumerate(self.servicios_disponibles, start=1):
            print(f"{i}. {servicio['nombre']} - ${servicio['precio']}")

        seleccion = input("Seleccione un servicio por número (o '0' para salir): ")
        try:
            seleccion = int(seleccion)
            if seleccion == 0:
                return
            servicio = self.servicios_disponibles[seleccion - 1]
            servicio_elegido = ServicioElegido(
                id=None,
                customer_id=customer_id,
                servicio_nombre=servicio['nombre'],
                precio=servicio['precio']
            )
            self.repo.guardar_servicio_elegido(db, servicio_elegido)
            print("Servicio registrado con éxito.")
        except (IndexError, ValueError):
            print("Selección inválida.")
