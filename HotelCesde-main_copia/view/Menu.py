from domain.Huesped import Customer
from application.CustomerService import CustomerService
from data.CustomerRepository import CustomerRepository
from data.ConexionMySQL import Conexion


class Menu:
    db = Conexion(host='localhost', port=3306, user='root', password="", database='hotel_cesde')
    db.connect()
    def __init__(self):
        self.customer = Customer(None,None,None,None,None,None,None,None)
        self.customer_service = CustomerService()
        self.customer_repo = CustomerRepository()


    def app(self):
        init = int(input("Presione 1 para iniciar: "))
        if init != 1:
            print("Iniciación cancelada.")
            return

        while True:
            print("\nMenú:")
            print("1. Login")
            print("2. Registro")
            print("3. Salir")
            option = input("Seleccione una opción: ")

            if option == '1':
                self.login()
            elif option == '2':
                self.customer_service.createCustomer(self.customer, self.db)
            elif option == '3':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción correcta.")


    def login(self):
        email = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        self.customer_service.login(self.db, email, password)

