#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 3 interfase pública de funcionalidades de una clase


class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
        print(f"La tarea '{tarea}' ha sido agregada.")

    def eliminarTarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"La tarea '{tarea}' ha sido eliminada.")
        else:
            print(f"La tarea '{tarea}' no se encuentra en la lista.")

    def mostrarTareas(self):
        if self.tareas:
            print("Tareas pendientes:")
            for tarea in self.tareas:
                print(f"- {tarea}")
        else:
            print("No hay tareas pendientes.")

listaTareas = ListaDeTareas()
listaTareas.mostrarTareas()
listaTareas.agregarTarea("Estudiar para el parcial")
listaTareas.agregarTarea("Comprar el almuerzo")
listaTareas.mostrarTareas()
listaTareas.eliminarTarea("Estudiar para el parcial")
listaTareas.mostrarTareas()
listaTareas.eliminarTarea("Ir al Supermercado")
