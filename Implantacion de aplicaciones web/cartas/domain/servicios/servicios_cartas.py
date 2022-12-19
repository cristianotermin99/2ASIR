from random import shuffle

from domain.modelo.Baraja import Baraja
from domain.modelo.Carta import Carta

class ServiciosCartas:
    def crear_baraja(self):
        baraja = Baraja()
        for palo in Carta.PALOS:
            for numero in Carta.NUMEROS:
                baraja.cartas.append(Carta(numero, palo))
        return baraja

    def mezclar_baraja(self,baraja : Baraja):
        shuffle(baraja.cartas)
    


    