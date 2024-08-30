from datetime import date

# Clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, fecha_ingreso):
        self.nombre = nombre  
        self.fecha_ingreso = fecha_ingreso  

    # Método para calcular los años trabajados
    def calcular_antiguedad(self):
        today = date.today()
        antiguedad = today.year - self.fecha_ingreso.year
        if today.month < self.fecha_ingreso.month or (today.month == self.fecha_ingreso.month and today.day < self.fecha_ingreso.day):
            antiguedad -= 1  
        return antiguedad

    # Método para calcular el bono por antigüedad
    def calcular_bono_antiguedad(self):
        if self.calcular_antiguedad() > 5:
            return 500  
        return 0

    # Método base para calcular el salario 
    def calcular_salario(self):
        pass

# Subclase para empleados de plaza fija
class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, fecha_ingreso, salario_base, comisiones):
        super().__init__(nombre, fecha_ingreso)
        self.salario_base = salario_base  
        self.comisiones = comisiones  

    # Método para calcular el salario de un empleado de plaza fija
    def calcular_salario(self):
        salario_total = self.salario_base + self.comisiones  
        salario_total += self.calcular_bono_antiguedad()  
        if self.calcular_antiguedad() > 5:
            salario_total += self.salario_base * 0.10  # Agregar 10% de paga al salario base
        return salario_total

# Subclase para empleados por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, fecha_ingreso, horas_trabajadas):
        super().__init__(nombre, fecha_ingreso)
        self.tarifa_hora = 8  # Tarifa fija de $8 por hora trabajada
        self.horas_trabajadas = horas_trabajadas 

    # Método para calcular el salario de un empleado por horas
    def calcular_salario(self):
        salario_total = self.tarifa_hora * self.horas_trabajadas 
        salario_total += self.calcular_bono_antiguedad()  
        if self.calcular_antiguedad() > 5:
            salario_total += salario_total * 0.10  # Agregar 10% de paga al salario total
        return salario_total

# Función para crear un empleado basado en la entrada del usuario
def crear_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    fecha_ingreso = date.fromisoformat(input("Ingrese la fecha de ingreso (YYYY-MM-DD): "))
    tipo_empleado = input("Ingrese 'F' para empleado de plaza fija o 'H' para empleado por horas: ").upper()

    if tipo_empleado == 'F':
        salario_base = float(input("Ingrese el salario base: "))
        comisiones = float(input("Ingrese las comisiones: "))
        return EmpleadoPlazaFija(nombre, fecha_ingreso, salario_base, comisiones)
    elif tipo_empleado == 'H':
        horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
        return EmpleadoPorHoras(nombre, fecha_ingreso, horas_trabajadas)
    else:
        print("Tipo de empleado no válido.")
        return None

# Crear una lista de empleados basada en la entrada del usuario
empleados = []
while True:
    empleado = crear_empleado()
    if empleado:
        empleados.append(empleado)
    continuar = input("¿Desea ingresar otro empleado? (S/N): ").upper()
    if continuar != 'S':
        break

# Calcular y mostrar los salarios
for empleado in empleados:
    print(f"Salario de {empleado.nombre}: {empleado.calcular_salario()}")


#En este codigo desarrollamos un sistema básico para calcular el salario de diferentes tipos de empleados en función de su antigüedad
#En la empresa y otras variables específicas de cada tipo de empleado. 

#Utilizamos POO para estructurar el código debido a las siguientes razones:
#Modularidad: La POO permite dividir el problema en partes más pequeñas y manejables. 
#En este caso, creamos una clase base Empleado y dos subclases EmpleadoPlazaFija y EmpleadoPorHoras. 
#Esto facilita la comprensión y el mantenimiento del código.
#Reutilización de Código: La herencia nos permite reutilizar código común entre diferentes tipos de empleados. 
#Por ejemplo, el cálculo de la antigüedad y el bono por antigüedad se realiza en la clase base Empleado, y ambas subclases heredan
#Estos métodos.
#Extensibilidad: Si en el futuro se agregan más tipos de empleados, podemos simplemente crear nuevas subclases sin modificar 
#El código existente

