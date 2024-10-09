#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 5 interfase pública de funcionalidades de una clase


class AlbumVirtual:
    def __init__(self):
        self.fotos = []

    def agregarFoto(self, foto):
        self.fotos.append(foto)
        print(f"La foto '{foto}' ha sido agregada al álbum.")

    def eliminarFoto(self, foto):
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f"La foto '{foto}' ha sido eliminada del álbum.")
        else:
            print(f"La foto '{foto}' no se encuentra en el álbum.")

    def mostrarFotos(self):
        if self.fotos:
            print("Fotos en el álbum:")
            for foto in self.fotos:
                print(f"- {foto}")
        else:
            print("El álbum está vacío.")

album = AlbumVirtual()
album.mostrarFotos()
print("_____________________________________")
album.agregarFoto("Parque del café")
album.agregarFoto("Cumpleaños")
album.mostrarFotos()
print("_____________________________________")
album.eliminarFoto("Parque del café")
album.mostrarFotos()
print("_____________________________________")
album.eliminarFoto("Univalle")
