# Pedido.py
from ElementoMenu import CrearMenu 
from typing import List

class Pedido:
    def __init__(self):
        self.menus: List[CrearMenu] = []  

    def agregar_menu(self, menu: CrearMenu):
        """Agrega un menú al pedido o incrementa la cantidad si ya existe."""
        for item in self.menus:
            if item.nombre == menu.nombre:
                item.cantidad += 1
                return
        
        # Crear una copia del menú con cantidad 1
        nuevo_menu = CrearMenu(
            nombre=menu.nombre,
            ingredientes=menu.ingredientes.copy(),
            precio=menu.precio,
            icono_path=menu.icono_path,
            cantidad=1
        )
        self.menus.append(nuevo_menu)

    def eliminar_menu(self, nombre_menu: str):
        """Elimina un menú del pedido."""
        self.menus = [menu for menu in self.menus if menu.nombre != nombre_menu]

    def mostrar_pedido(self):
        """Muestra el contenido del pedido."""
        if not self.menus:
            print("El pedido está vacío.")
            return
        
        print("Pedido actual:")
        for menu in self.menus:
            print(f"  - {menu.nombre}: {menu.cantidad} x ${menu.precio:.2f} = ${menu.cantidad * menu.precio:.2f}")
        
        total = self.calcular_total()
        print(f"Total: ${total:.2f}")

    def calcular_total(self) -> float:
        """Calcula el total del pedido."""
        return sum(menu.precio * menu.cantidad for menu in self.menus)

    def limpiar_pedido(self):
        """Limpia todo el pedido."""
        self.menus.clear()

    def __len__(self):
        """Retorna la cantidad total de ítems en el pedido."""
        return sum(menu.cantidad for menu in self.menus)

    def __str__(self):
        return f"Pedido con {len(self)} ítems - Total: ${self.calcular_total():.2f}"
