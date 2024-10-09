#Laboratorio 
#Mao Ying Gomez Uribe
#Acitvidad 5 Estado interno de una clase

class ElCarroDeAra:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)
        print(f"'{producto}' ha sido añadido al carrito.")

    def eliminarProducto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"'{producto}' ha sido eliminado del carrito.")
        else:
            print(f"'{producto}' no está en el carrito.")

    def mostrarProductos(self):
        if self.productos:
            print("Productos en el carrito:")
            for producto in self.productos:
                print(f"- {producto}")
        else:
            print("El carrito está vacío.")


carrito = ElCarroDeAra()
carrito.mostrarProductos()
carrito.agregarProducto("Café")
carrito.agregarProducto("Leche")
carrito.mostrarProductos()
print("__________________________________")
carrito.eliminarProducto("Café")
print("__________________________________")
carrito.mostrarProductos()
print("__________________________________")
carrito.eliminarProducto("Queso")  
print("__________________________________")
