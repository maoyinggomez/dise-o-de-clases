#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 1 interfase pública de funcionalidades de una clase

class Cafetera:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.nivelActual = 0

    def llenarCafetera(self):
        self.nivelActual = self.capacidad
        print("La cafetera ha sido llenada al máximo.")

    def servirCafe(self):
        if self.nivelActual > 0:
            self.nivelActual -= 1
            print("Se ha servido una taza de café.")
        else:
            print("No queda café en la cafetera.")

    def mostrarNivel(self):
        print(f"Quedan {self.nivelActual} tazas de café en la cafetera.")

cafetera = Cafetera(5)
cafetera.mostrarNivel()
print("__________________________________")
cafetera.llenarCafetera()
print("__________________________________")
cafetera.mostrarNivel()
print("__________________________________")
cafetera.servirCafe()
print("__________________________________")
cafetera.mostrarNivel()
