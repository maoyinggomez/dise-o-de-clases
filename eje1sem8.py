#Laboratorio 
#Mao Ying Gomez Uribe
#Actividad 1 Estado interno de una clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.estado = "Despierta"

    def dormir(self):
        self.estado = "Durmiendo"

    def despertar(self):
        self.estado = "Despierta"

    def mostrar_estado(self):
        print(f"{self.nombre}, de {self.edad} años, está {self.estado}.")


persona = Persona("Mao Ying", 26)
persona.dormir()
persona.mostrar_estado()
persona.despertar()
persona.mostrar_estado()
