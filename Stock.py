from Ingrediente import Ingrediente

class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        for item in self.lista_ingredientes:
            if item.nombre.lower() == ingrediente.nombre.lower():
                item.cantidad += ingrediente.cantidad
                print(f" Stock de '{ingrediente.nombre}' actualizado a {item.cantidad}.")
                return

    def eliminar_ingrediente(self, nombre_ingrediente):
        for item in self.lista_ingredientes:
            if item.nombre.lower() == nombre_ingrediente.lower():
                self.lista_ingredientes.remove(item)
                print(f" Ingrediente '{nombre_ingrediente}' eliminado del stock.")
                return
        print(f" Ingrediente '{nombre_ingrediente}' no encontrado en el stock.") 

    def verificar_stock(self):
        for item in self.lista_ingredientes:
            print(f" Ingrediente: {item.nombre}, Cantidad: {item.cantidad}")

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        pass

    def obtener_elementos_menu(self):
        pass

