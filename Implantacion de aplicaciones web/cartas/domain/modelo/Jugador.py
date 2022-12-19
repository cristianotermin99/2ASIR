from dataclasses import dataclass, field
from domain.modelo.Carta import Carta

@dataclass
class Jugador:
    nombre : str
    apellidos : str
    carta : Carta = (Carta(0,0))
    puntos : int = 0
    

