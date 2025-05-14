

from domain.Huesped import Customer
from data.CustomerRepository import CustomerRepository

class CustomerService:

    def __init__(self):
        self.customer_repository = CustomerRepository()
        self.customer = Customer(None,None,None,None,None,None,None,None)

    def createCustomer(self, customer, db):
        print("\nCustomer:\n")
        
        id = int(input("Ingrese su identificacion: "))
        customer.id = id
        name = input("Ingrese su nombre: ")
        customer.name = name
        last_name = input("Ingrese su apellido: ")
        customer.last_name = last_name
        email = input("Ingrese su correo: ")
        customer.email = email
        password = input("Ingrese su password: ")
        customer.password = password
        status = input("Ingrese True Si esta activo:")
        customer.status = status
        origin = input("Ciudad de Origen: ")
        customer.origin = origin
        occupation = input("Ocupación: ")
        customer.occupation = occupation

        self.customer_repository.createCustomerReposity(db,customer)


    def login(self, db, email, password):
        customer = self.customer_repository.get_customer_by_credentials(db, email, password)
        if customer:
            print("Login exitoso")
            return customer
        else:
            print("Error en el login")
            return None


