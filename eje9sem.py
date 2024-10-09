#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 4 interfase pública de funcionalidades de una clase

class Temporizador:
    def __init__(self, tiempoRestante):
        self.tiempoRestante = tiempoRestante
        self.pausado = False

    def iniciarTemporizador(self):
        if not self.pausado:
            print(f"El temporizador ha sido iniciado con {self.tiempoRestante} segundos restantes.")
        else:
            print(f"El temporizador ha sido reanudado con {self.tiempoRestante} segundos restantes.")
            self.pausado = False

    def pausarTemporizador(self):
        if not self.pausado:
            print(f"El temporizador ha sido pausado con {self.tiempoRestante} segundos restantes.")
            self.pausado = True
        else:
            print("El temporizador ya está pausado.")

    def mostrarTiempoRestante(self):
        print(f"Tiempo restante: {self.tiempoRestante} segundos.")


temporizador = Temporizador(120)
temporizador.mostrarTiempoRestante()
print("_____________________________________")
temporizador.iniciarTemporizador()
print("_____________________________________")
temporizador.mostrarTiempoRestante()
