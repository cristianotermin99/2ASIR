def pedirNumero():
    try:
        numero=int(input("Introduce el primer numero entre 1 y 10: "))
        if int(numero)<10 and int(numero)>0:
            return numero
        else:
            return "El numero introducido no esta entre el rango valido"
    except ValueError:
        print("El valor introducido no es un numero. ")


numero1=pedirNumero()
numero2=pedirNumero()
if numero1 != "Alguno de los numeros introducidos no esta entre el rango valido" and numero1 != "El numero introducido no esta entre el rango valido":
    suma=int(numero1)+int(numero2)
    print(numero1," + ",numero2," = ",suma)
else:
    print(numero1)












