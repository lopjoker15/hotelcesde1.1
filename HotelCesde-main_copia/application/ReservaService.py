import datetime

# Lista para almacenar las reservas
reservas = []

# Función para hacer una reserva
def hacer_reserva():
    print("\n--- Hacer una Reserva ---")
    
    nombre = input("Ingresa tu nombre: ")
    fecha_entrada = input("Fecha de entrada (YYYY-MM-DD): ")
    fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")

    try:
        fecha_entrada = datetime.datetime.strptime(fecha_entrada, "%Y-%m-%d")
        fecha_salida = datetime.datetime.strptime(fecha_salida, "%Y-%m-%d")
    except ValueError:
        print("Fecha inválida. Intenta de nuevo.")
        return

    if fecha_entrada >= fecha_salida:
        print("La fecha de salida debe ser posterior a la de entrada.")
        return
    
    tipo_habitacion = input("Tipo de habitación (Individual, Doble, Suite): ").capitalize()

    reserva = {
        "nombre": nombre,
        "fecha_entrada": fecha_entrada,
        "fecha_salida": fecha_salida,
        "tipo_habitacion": tipo_habitacion
    }
    
    reservas.append(reserva)
    print(f"\nReserva realizada con éxito para {nombre} en una habitación {tipo_habitacion}.")
    print(f"Entrada: {fecha_entrada.strftime('%Y-%m-%d')}, Salida: {fecha_salida.strftime('%Y-%m-%d')}")