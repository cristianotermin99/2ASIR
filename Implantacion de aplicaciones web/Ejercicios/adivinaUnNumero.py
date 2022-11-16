import random

numeroAleatorio=random.randint(1,100)
numeroIntroducido=-1
numeroIntentos=0





while numeroAleatorio != numeroIntroducido and numeroIntentos<10:
    numeroIntroducido=int(input("Introduce un numero entre 1 y 100: "))
    numeroIntentos+=1
    if numeroIntroducido<numeroAleatorio:
        print("El numero que has introducido es menor. Introduce un numero mayor. Llevas ", numeroIntentos, " intentos")
    elif numeroIntroducido>numeroAleatorio:
        print("El numero que has introducido es mayor. Introduce un numero menor. Llevas ", numeroIntentos, " intentos")




if numeroAleatorio==numeroIntroducido:
    print("Has acertado el numero era ", numeroAleatorio)
else:
    print("Has perdido con 10 fallos")

