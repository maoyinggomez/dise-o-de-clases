#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 3 Estado interno de una clase

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto y ahora está disponible.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

    def mostrar_estado(self):
        estado = "disponible" if self.disponible else "prestado"
        print(f"El libro '{self.titulo}' de {self.autor} está actualmente {estado}.")

libro1 = Libro("El Alquimista", "Paulo Coelho")
libro1.mostrar_estado()
libro1.prestar()
libro1.mostrar_estado()
libro1.prestar()
libro1.devolver()
libro1.mostrar_estado()
