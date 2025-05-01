from domain.Pago import Pago   # type: ignore

class PagoService:

    def __init__(self):
        self.pagos = []  
  
    def createPago(self):
        """
        Crea un nuevo pago interactuando con el usuario.
        """
        id_pago = int(input("Ingrese el ID del pago: "))
        monto = float(input("Ingrese el monto del pago: "))
        metodo_pago = input("Ingrese el método de pago (ejemplo: tarjeta, efectivo): ")
        cliente_id = int(input("Ingrese el ID del cliente que realiza el pago: "))

        
        nuevo_pago = Pago(id_pago, monto, metodo_pago, cliente_id)
        self.pagos.append(nuevo_pago)  
        print("Pago registrado exitosamente.")

    def obtenerPagosPorCliente(self, cliente_id):
        """
        Obtiene todos los pagos realizados por un cliente específico.

        :param cliente_id: ID del cliente.
        :return: Lista de pagos realizados por el cliente.
        """
        pagos_cliente = [p for p in self.pagos if p.cliente_id == cliente_id]
        if pagos_cliente:
            print(f"Pagos encontrados para el cliente con ID {cliente_id}:")
            for pago in pagos_cliente:
                print(f"ID: {pago.id}, Monto: {pago.monto}, Método: {pago.metodo_pago}")
        else:
            print(f"No se encontraron pagos para el cliente con ID {cliente_id}.")
        return pagos_cliente