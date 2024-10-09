#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 4 Estado interno de una clase

class Termostato:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def aumentar(self, grados):
        self.temperatura += grados

    def disminuir(self, grados):
        self.temperatura -= grados

    def mostrar_temperatura(self):
        print(f"La temperatura actual es {self.temperatura}°C")


termostato = Termostato(25)
termostato.mostrar_temperatura()
print("_____________________________________")
termostato.aumentar(5)
termostato.mostrar_temperatura()
print("_____________________________________")
termostato.disminuir(3)
termostato.mostrar_temperatura()
