class Habitacion:
    def __init__(self, tipo, precio):
        # Inicializa el tipo y el precio de la habitación
        self.tipo = tipo
        self.precio = precio

class Cliente:
    def __init__(self, nombre, noches, habitacion, servicios_extra=[]):
        # Inicializa el nombre del cliente, el número de noches, la habitación y los servicios extra
        self.nombre = nombre
        self.noches = noches
        self.habitacion = habitacion
        self.servicios_extra = servicios_extra
    
    def calcular_total(self):
        # Calcula el costo total de la estancia incluyendo los servicios extra
        total = self.noches * self.habitacion.precio
        for servicio in self.servicios_extra:
            total += servicio['precio']
        return total
    
    def generar_factura(self):
        # Genera e imprime una factura detallada para el cliente
        print(f"Factura para {self.nombre}:")
        print(f"Habitación: {self.habitacion.tipo} - {self.noches} noches a {self.habitacion.precio} por noche")
        for servicio in self.servicios_extra:
            print(f"Servicio extra: {servicio['nombre']} - {servicio['precio']}")
        print(f"Total a pagar: {self.calcular_total()}")

class Hotel:
    def __init__(self):
        # Inicializa las habitaciones y los servicios extra disponibles en el hotel
        self.habitaciones = [
            Habitacion("Simple", 100),
            Habitacion("Doble", 150),
            Habitacion("Suite", 300)
        ]
        self.servicios_extra = [
            {"nombre": "Piscina", "precio": 50},
            {"nombre": "Cancha de Golf", "precio": 100}
        ]

    def mostrar_habitaciones(self):
        # Muestra las opciones de habitaciones disponibles
        print("Opciones de habitaciones:")
        for idx, habitacion in enumerate(self.habitaciones):
            print(f"{idx + 1}. {habitacion.tipo} - {habitacion.precio} por noche")

    def mostrar_servicios(self):
        # Muestra los servicios extra disponibles
        print("Servicios extra disponibles:")
        for idx, servicio in enumerate(self.servicios_extra):
            print(f"{idx + 1}. {servicio['nombre']} - {servicio['precio']}")

    def elegir_habitacion(self):
        # Permite al usuario elegir una habitación de la lista
        self.mostrar_habitaciones()
        opcion = int(input("Elija una habitación (número): ")) - 1
        return self.habitaciones[opcion]

    def elegir_servicios(self):
        # Permite al usuario elegir servicios extra de la lista
        self.mostrar_servicios()
        servicios_elegidos = []
        while True:
            opcion = input("Elija un servicio extra (número) o 'F' para terminar: ")
            if opcion.upper() == 'F':
                break
            else:
                servicios_elegidos.append(self.servicios_extra[int(opcion) - 1])
        return servicios_elegidos

    def check_in(self):
        # Realiza el proceso de check-in para un cliente, incluyendo la selección de habitación y servicios, y genera la factura
        nombre = input("Ingrese su nombre: ")
        habitacion = self.elegir_habitacion()
        noches = int(input("Ingrese el número de noches: "))
        servicios_extra = self.elegir_servicios()
        
        cliente = Cliente(nombre, noches, habitacion, servicios_extra)
        cliente.generar_factura()

# Crear una instancia de Hotel y realizar el check-in
hotel = Hotel()
hotel.check_in()


#El problema involucra la gestión de un proceso típico de check-in en un hotel, incluyendo la selección de habitaciones,
# la gestión de servicios adicionales, y la generación de una factura. Dado que estos elementos (habitaciones, clientes, servicios,
# hotel) son claramente identificables y poseen características y comportamientos propios, se optó por una solución basada 
# en Programación Orientada a Objetos (POO).

#Se usaron 3 clases para organizar bien el código. 
# Cada clase se encarga de una cosa específica: una se encarga de las habitaciones, otra del cliente, 
# y otra de manejar todo el proceso en el hotel.
#  Esto hace que el código sea más fácil de entender, modificar y mantener.

# Clase Habitacion:
#Representa una habitación del hotel. Cada habitación tiene un tipo (como "Simple" o "Suite") y un precio por noche.

#Clase Cliente:
#Representa al cliente que se queda en el hotel. Aquí se guarda su nombre, cuántas noches se queda, qué habitación eligió 
# y si pidió algún servicio extra.

#Clase Hotel:
#Es la parte que maneja todo el proceso de check-in del cliente, desde elegir la habitación hasta añadir servicios extras.