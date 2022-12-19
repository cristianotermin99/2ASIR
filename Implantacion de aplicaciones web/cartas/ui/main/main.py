from operator import attrgetter

from domain.modelo.Baraja import Baraja
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
            if i+j<40:
                jugadores[j].carta = baraja.cartas[i+j]
                print(jugadores[j].carta, "para",jugadores[j].nombre)
        # un punto al jugador que la tenga mas grande
        cartaGanadora : Carta = jugadores[0].carta
        for j in range (0,cantidadJugadores):
            if jugadores[j].carta.valor.value>=cartaGanadora.valor.value:
                cartaGanadora=jugadores[j].carta
        for j in range (0,cantidadJugadores):
            if jugadores[j].carta.valor.value==cartaGanadora.valor.value:
                jugadores[j].puntos+=1
                print("Punto para ", jugadores[j].nombre)
    # al final cuando se acaba la baraja se dice quien gana
    puntosMaximos=0
    for i in range(0,cantidadJugadores):
            if jugadores[i].puntos>=puntosMaximos:
                puntosMaximos=jugadores[i].puntos
    
            
    print("--------------------------------")   
    for j in range (0,cantidadJugadores):
            print(jugadores[j].nombre,"ha hecho",jugadores[j].puntos,"puntos")
    print("--------------------------------")  
    for j in range (0,cantidadJugadores):
            if jugadores[j].puntos==puntosMaximos:
                print("Ha ganado ", jugadores[j].nombre)
    print("--------------------------------")  


