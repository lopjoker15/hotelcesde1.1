from domain.Servicio import Servicio

class ServicioRepository:
    def listar_servicios(self):
        servicios = [
            Servicio(1, "Restaurante"),
            Servicio(2, "Gimnasio"),
            Servicio(3, "Spa"),
            Servicio(4, "Piscina"),
            Servicio(5, "Wi-Fi"),
            Servicio(6, "Transporte al aeropuerto"),
        ]
        return servicios
