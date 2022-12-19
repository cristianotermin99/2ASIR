from operator import attrgetter

from domain.modelo.baraja import Baraja
from domain.modelo.Jugador import Jugador
from domain.modelo.Carta import Carta
from domain.servicios.servicios_cartas import ServiciosCartas


# ejecucion cosas
def main():
    servicios_cartas: ServiciosCartas = ServiciosCartas()
    baraja: Baraja = servicios_cartas.crear_baraja()
    

    servicios_cartas.mezclar_baraja(baraja)

    # Pedir n jugadores
    cantidadJugadores = int(input("Cuantos jugadores??: "))
    # Combat cartas

    jugadores : list[Jugador] = []
    for i in range(0,cantidadJugadores):
        nombre = input("Introduce tu nombre: ")
        apellido = input("Introduce tus apellidos: ")
        jugadores.append(Jugador(nombre, apellido))
        
    for i in range (0,40,cantidadJugadores):
        # sacar cartas, una para cada jugador
        for j in range (0,cantidadJugadores):
            jugadores[j].carta = baraja.cartas[i+j]
            print(jugadores[j].carta, "para",jugadores[j].nombre)
        # un punto al jugador que la tenga mas grande
        cartaGanadora : Carta = Carta(0,0)
        for j in range (0,cantidadJugadores):
            if jugadores[j].carta.valor.value>=cartaGanadora.valor.value:
                cartaGanadora=jugadores[j].carta
        for j in range (0,cantidadJugadores):
            if jugadores[j].carta.valor.value==cartaGanadora.valor.value:
                jugadores[j].puntos+=1
    # al final cuando se acaba la baraja se dice quien gana
    jugadorGanador : Jugador=Jugador("", "")
    for i in range(0,cantidadJugadores-1):
            if jugadores[i].puntos>jugadores[i+1]:
                jugadorGanador=jugadores[i]
            else:
                jugadorGanador=jugadores[i+1]
    print("Ha ganado ", jugadorGanador.nombre)


