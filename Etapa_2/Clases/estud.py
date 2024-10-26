class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    
    def promedio(self):
        if len(self.calificaciones) > 0:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0
    
    def mostrar_info(self):
        promedio = self.promedio()
        print(f"Nombre: {self.nombre}, Promedio: {promedio:.2f}")

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("David")

# Agregar algunas calificaciones
estudiante1.agregar_calificacion(65)
estudiante1.agregar_calificacion(70)
estudiante1.agregar_calificacion(78)

# Mostrar informacion
estudiante1.mostrar_info()
