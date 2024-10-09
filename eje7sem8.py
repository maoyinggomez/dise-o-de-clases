#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 2 interfase pública de funcionalidades de una clase

class BibliotecaVirtualKindle:
    def __init__(self):
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f"El libro '{libro}' ha sido agregado a la biblioteca.")

    def eliminarLibro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"El libro '{libro}' ha sido eliminado de la biblioteca.")
        else:
            print(f"El libro '{libro}' no está en la biblioteca.")

    def mostrarLibros(self):
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro}")
        else:
            print("No hay libros en la biblioteca.")

biblioteca = BibliotecaVirtualKindle()
biblioteca.mostrarLibros()
print("________________________________________")
biblioteca.agregarLibro("La Bruja")
biblioteca.agregarLibro("El Aprendiz del brujo")
print("________________________________________")
biblioteca.mostrarLibros()
print("________________________________________")
biblioteca.eliminarLibro("El Alquimista")
print("________________________________________")
biblioteca.mostrarLibros()
print("________________________________________")
biblioteca.eliminarLibro("Don Quijote de la Mancha")
