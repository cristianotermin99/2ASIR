import random

numeroAleatorio=random.randint(1,100)
numeroIntroducido=-1
numeroIntentos=0
dineroInicialJugador=0
dineroInicialJugador=int(input("Introduce la cantidad de dinero inicial con la que vas a jugar: "))
dineroFinalJugador=dineroInicialJugador
dineroApostadoEstaPartida=0
seguir=1
while seguir==1:
    dineroApostadoEstaPartida=int(input("Introduce la cantidad de dinero que quieres apostar esta partida: "))
    if dineroApostadoEstaPartida<dineroFinalJugador:
        while numeroAleatorio != numeroIntroducido and numeroIntentos<10:
        
            numeroIntroducido=int(input("Introduce un numero entre 1 y 100: "))
            numeroIntentos+=1
            if numeroIntroducido<numeroAleatorio:
                print("El numero que has introducido es menor. Introduce un numero mayor. Llevas ", numeroIntentos, " intentos")
            elif numeroIntroducido>numeroAleatorio:
                print("El numero que has introducido es mayor. Introduce un numero menor. Llevas ", numeroIntentos, " intentos")

        if numeroAleatorio==numeroIntroducido:
            dineroFinalJugador+=dineroApostadoEstaPartida
            print("Has acertado el numero era ", numeroAleatorio)
            print("Has ganado ",dineroApostadoEstaPartida, " euros") 
        else:
            dineroFinalJugador-=dineroApostadoEstaPartida
            print("Has perdido con 10 fallos")
            print("Has perdido ",dineroApostadoEstaPartida, " euros")
    else:
        print("No puedes apostar mas dinero del que tienes! ")

    print("Tienes ",dineroFinalJugador, " euros")  
    seguir=int(input("Deseas continuar jugando? 1. Si    2.No:    "))

