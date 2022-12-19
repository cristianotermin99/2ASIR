from dataclasses import dataclass, field
from domain.modelo.Carta import Carta

@dataclass
class Jugador:
    nombre : str
    apellidos : str
    carta : Carta = (Carta(0,0))
    puntos : int = 0
    

    def nombre_completo(self):  
        return self.nombre + " " + self.apellidos

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + str(self.puntos)
