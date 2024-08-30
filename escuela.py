from datetime import datetime

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial_asistencia = []

    def agregarAsistencia(self, asistencia):
        self.historial_asistencia.append(asistencia)

# Clase Docente
class Docente:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase Asistencia
class Asistencia:
    def __init__(self, fecha, estado, razon=None):
        self.fecha = fecha
        self.estado = estado
        self.razon = razon

# Clase RegistroAsistencia
class RegistroAsistencia:
    def __init__(self):
        self.estudiantes = {}

    def registrarestudiante(self, nombre):
        if nombre in self.estudiantes:
            print(f"{nombre} ya está registrado.")
            return self.estudiantes[nombre]
        nuevoestudiante = Estudiante(nombre)
        self.estudiantes[nombre] = nuevoestudiante
        print(f"Estudiante {nombre} registrado.")
        return nuevoestudiante

    def asignar_asistencia(self, estudiante, estado, razon=None):
        fecha = datetime.now().strftime("%d/%m/%Y")  
        nuevaAsistencia = Asistencia(fecha, estado, razon)
        estudiante.agregar_asistencia(nuevaAsistencia)
        print(f"Asistencia registrada para {estudiante.nombre} el {fecha}.")

    def mostrarAsistenciaEstudiantes(self):
        if not self.estudiantes:
            print("No hay registro de estudiantes.")
            return
        for estudiante in self.estudiantes.values():
            if estudiante.historial_asistencia:
                print(f"\nEstudiante: {estudiante.nombre}")
                for asistencia in estudiante.historial_asistencia:
                    print(f"  Fecha: {asistencia.fecha}, Estado: {asistencia.estado}, Razón: {asistencia.razon if asistencia.razon else 'N/A'}")

docente = Docente("Prof. Pérez")
registroAsistencia = RegistroAsistencia()

while True:
    print("\nMenú:")
    print("1. Registrar asistencia del estudiante")
    print("2. Mostrar asistencia de los estudiantes")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del estudiante: ")
        estudiante = registroAsistencia.registrarEstudiante(nombre)
        estado = input("Ingrese el estado de asistencia (Asistió, Falta, Permiso): ")
        razon = None
        if estado.lower() == "permiso":
            razon = input("Ingrese la razón del permiso: ")
        registroAsistencia.asignar_asistencia(estudiante, estado, razon)

    elif opcion == '2':
        registroAsistencia.mostrarAsistenciaEstudiantes()

    elif opcion == '3':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor intente de nuevo.")

#se utilizo el poo porque al ser una programacion orientada a objetos se utilizo la creacion de clases 
#que representa las entidades de docentes, estudiantes y para crear la clase de asistencia, en este caso 
# cada clase tiene su propia funcion pero tambien permite trabajar con otra clase diferente 

#este programa funciona para que el profesor a la hora de pasar lista vaya registrando el nombre de los estudiantes 
#les asigne si asistio o falto a la clase, en caso de haber mandado permiso el programa permite ingresar la razon de de la falta
#  para de estar manera llevar el registro necesario y presentarselo a al director
