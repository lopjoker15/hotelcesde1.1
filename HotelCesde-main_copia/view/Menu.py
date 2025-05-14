from domain.Huesped import Customer
from application.CustomerService import CustomerService
from data.CustomerRepository import CustomerRepository
from data.ConexionMySQL import Conexion
from application.ReservaService import ReservaService
from application.ServicioService import ServicioService
from application.PagoService import PagoService


class Menu:
    def __init__(self):
        self.db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_cesde')
        self.db.connect()
        self.customer = Customer(None, None, None, None, None, None, None, None)
        self.customer_service = CustomerService()
        self.customer_repo = CustomerRepository()
        self.reserva_service = ReservaService()
        self.servicio_service = ServicioService()
        self.pago_service = PagoService()
        self.logged_in = False  # Estado de sesión

    def app(self):
        init = int(input("Presione 1 para iniciar: "))
        if init != 1:
            print("Iniciación cancelada.")
            return
    
        while True:
            if not self.logged_in:
                print("\nMenú:")
                print("1. Login")
                print("2. Registro")
                print("5. Salir")
                option = input("Seleccione una opción: ")
    
                if option == '1':
                    self.login()
                elif option == '2':
                    self.customer_service.createCustomer(self.customer, self.db)
                elif option == '5':
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción correcta.")
            else:
                print("\nMenú - Usuario autenticado:")
                print("1. Ver servicios")
                print("2. Hacer una reserva")
                print("3. Salir")
                option = input("Seleccione una opción: ")
    
                if option == '1':
                     self.servicio_service.mostrar_servicios(self.db, self.customer.id)
                elif option == '2':
                    self.reserva_service.hacer_reserva(self.db)
                elif option == '3':
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción correcta.")

    def login(self):
      email = input("Ingrese su correo: ")
      password = input("Ingrese su contraseña: ")
      customer = self.customer_service.login(self.db, email, password)
      if customer:
          print("Login exitoso.")
          self.logged_in = True
          self.customer = customer  # Guarda al cliente actual
      else:
          print("Credenciales inválidas.")
          self.logged_in = False


