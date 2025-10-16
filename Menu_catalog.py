from typing import List
from ElementoMenu import CrearMenu
from Ingrediente import Ingrediente
from IMenu import IMenu

def get_default_menus() -> List[IMenu]:
    return [
        CrearMenu(
            "Completo",
            [
                Ingrediente("Vienesa","unid", 1),
                Ingrediente("Pan de completo","unid", 1),
                Ingrediente("Palta","unid",1),
                Ingrediente("Tomate","unid",1),
            ],
            precio=1800,
            icono_path="IMG/icono_hotdog_sin_texto_64x64.png",
        ),
        CrearMenu(
            "Papa frita",
            [
                Ingrediente("papas","unid", 5),
            ],
            precio=500,
            icono_path= "IMG/icono_papas_fritas_64x64.png"

        ),

        CrearMenu(
            "Pepsi",
            [
                Ingrediente("Pepsi","unid", 1),
            ],
            precio=1100,
            icono_path= "IMG/icono_cola_64x64.png"

        ),

        CrearMenu(
            "Coca-cola",
            [
                Ingrediente("Coca-cola","unid", 1),
            ],
            precio=1300,
            icono_path= "IMG/icono_cola_lata_64x64.png"

        ),

        CrearMenu(
            "Humburguesa",
            [
                Ingrediente("Pan de hambuerguesa","unid", 1),
                Ingrediente("Lamnina de queso","unid", 1),
                Ingrediente("Churrasco de carne","unid", 1),
                
            ],
            precio=3500,
            icono_path= "IMG/icono_hamburguesa_negra_64x64.png"

        ),

        CrearMenu(
            "Empanada de carne",
            [
                Ingrediente("Masa de empanadas","unid", 1),
                Ingrediente("Carne de Vacuno","unid", 1),
                Ingrediente("Cabolla","unid", 1),
                
            ],
            precio=2000,
            icono_path= "IMG/icono_empanada_carne_64x64.png"
        ),

        CrearMenu(
            "Empanada de queso",
            [
                Ingrediente("Masa de empanadas","unid", 1),
                Ingrediente("Queso","unid", 1),
                
            ],
            precio=2000,
            icono_path= "IMG/icono_empanada_queso_64x64.png"
        ),

        CrearMenu(
            "Panqueques",
            [
                Ingrediente("Panqueques","unid", 2),
                Ingrediente("Manjar","unid", 1),
                Ingrediente("Azucar flor","unid", 1),
                
            ],
            precio=2000,
            icono_path= "IMG/icono_panqueques_64x64 (1).png"

        ),

        CrearMenu(
            "Pollo Frito",
            [
                Ingrediente("Presa de pollo","unid", 1),
                Ingrediente("Porcion de Harina","unid", 1),
                Ingrediente("Porcion de aceite","unid", 1),
                
            ],
            precio=2800,
            icono_path= "IMG/icono_pollo_frito_64x64.png"

        ),
        
        CrearMenu(
            "Ensalada",
            [
                Ingrediente("Lechuga","unid", 1),
                Ingrediente("Tomate","unid", 1),
                Ingrediente("Zanahoria","unid", 1),
                
            ],
            precio=1500,
            icono_path= "IMG/icono_ensalada_64x64.png"

        ),
        
    ]