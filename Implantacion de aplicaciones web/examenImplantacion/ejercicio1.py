#Se pide un programa para el mundial de dados que va a hacer ibai con la
#colaboracion de Iker casillas. El Juego es entre dos jugadores, estos juegan la eliminatoria al
#mejor de 5, si uno gana 3 ya ha ganado. En cada partida antes de tirar los dados, un jugador
#dice si elige par o impar, el jugador que elige cambia de partida en partida, primero uno y
#después el otro, con turnos alternativos. Se tiran dos dados, simulados con un random, y si
#el dado tiene lo que eligio el jugador gana, sino gana el otro la partida. El primer jugador
#que dice si quiere par o impar en la eliminatoria se resolverá tirando una moneda, simula
#con random, cara o cruz.
#a. RESUMEN, se piden los nombres de los jugadores
#b. RESUMEN, se pide al primero que elija cara o cruz y se lanza la moneda, si acierta
#empieza el, si no el otro.
#c. RESUMEN, Por turnos alternan los jugadores van eligiendo par o impar, se tiran los
#dados y en el que acierte gana un minipunto
#d. RESUMEN el que llege a 3 puntos gana
#e. RESUMEN, se pone en consola al ganador.

import random


nombreJugador1=input("Introduce el nombre del jugado 1: ")
nombreJugador2=input("Introduce el nombre del jugado 2: ")
turno=0
eleccionMonedaJugador1=input(nombreJugador1+" elige cara o cruz: ")
moneda=random.randint(0,1)
jugadorComienzo=""

if moneda==0:
    if eleccionMonedaJugador1.upper()=="CARA":
        print("Ha salido cara por lo que el primero en jugar será: ",nombreJugador1)
        jugadorComienzo=nombreJugador1
    elif eleccionMonedaJugador1.upper()=="CRUZ":
        print("Ha salido cara por lo que el primero en jugar será: ",nombreJugador2)
        jugadorComienzo=nombreJugador2
else:
    if eleccionMonedaJugador1.upper()=="CRUZ":
        print("Ha salido cruz por lo que el primero en jugar será: ",nombreJugador1)
        jugadorComienzo=nombreJugador1
    elif eleccionMonedaJugador1.upper()=="CARA":
        print("Ha salido cruz por lo que el primero en jugar será: ",nombreJugador2)
        jugadorComienzo=nombreJugador2



puntosJugador1=0
puntosJugador2=0

while (puntosJugador1<3 and puntosJugador2<3):
    eleccionParOImpar=""
    dadoNumeroEntreUnoYSeis=random.randint(1,6)
    if jugadorComienzo==nombreJugador1:
        eleccionParOImpar=input(nombreJugador1+ " par o impar?: ")
        print("Ha salido el numero ",dadoNumeroEntreUnoYSeis)
        if eleccionParOImpar.upper()=="PAR":
            if dadoNumeroEntreUnoYSeis%2==0:
                puntosJugador1+=1
                print("El numero es par has acertado, "+nombreJugador1)
            else:
                puntosJugador2+=1
                print("El numero es impar has fallado, "+nombreJugador1)
        elif eleccionParOImpar.upper()=="IMPAR":
            if dadoNumeroEntreUnoYSeis%2!=0:
                puntosJugador1+=1
                print("El numero es impar has acertado, "+nombreJugador1)
            else:
                puntosJugador2+=1
                print("El numero es par has fallado, "+nombreJugador1)
        jugadorComienzo=nombreJugador2
    else:
        eleccionParOImpar=input(nombreJugador2+ " par o impar?: ")
        print("Ha salido el numero ",dadoNumeroEntreUnoYSeis)
        if eleccionParOImpar.upper()=="PAR":
            if dadoNumeroEntreUnoYSeis%2==0:
                puntosJugador2+=1
                print("El numero es par has acertado, "+nombreJugador2)
            else:
                puntosJugador1+=1
                print("El numero es impar has fallado, "+nombreJugador2)
        elif eleccionParOImpar.upper()=="IMPAR":
            if dadoNumeroEntreUnoYSeis%2!=0:
                puntosJugador2+=1
                print("El numero es impar has acertado, "+nombreJugador2)
            else:
                puntosJugador1+=1
                print("El numero es par has fallado, "+nombreJugador2)
        jugadorComienzo=nombreJugador1

    print(nombreJugador1+" lleva ",puntosJugador1," puntos")
    print(nombreJugador2+" lleva ",puntosJugador2," puntos")
    
    
if puntosJugador1==3:
    print("Has gannadooooo "+nombreJugador1)
else:
    print("Has gannadooooo "+nombreJugador2)



