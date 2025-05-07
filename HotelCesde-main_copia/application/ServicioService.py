from data.ServicioRepository import ServicioRepository

class ServicioService:
    def __init__(self):
        self.repo = ServicioRepository()

    def mostrar_servicios(self):
        servicios = self.repo.listar_servicios()
        print("\n--- Servicios del Hotel ---")
        for s in servicios:
            print(f"{s.id}. {s.nombre}")