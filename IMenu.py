# IMenu.py
from typing import Protocol, List, Optional
from Ingrediente import Ingrediente
from Stock import Stock

class IMenu(Protocol):
    """Interfaz para los elementos del menú."""
    # Atributos requeridos
    nombre: str
    ingredientes: List[Ingrediente]
    precio: float
    icono_path: Optional[str]
    cantidad: int
    # Métodos requeridos
    def esta_disponible(self, stock: Stock) -> bool:
        """Verifica si el menú está disponible según el stock."""
        ...