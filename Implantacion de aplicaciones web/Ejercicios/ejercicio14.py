tipoIntroducido=input("Introduce tipo A o B: ")
tamañoIntroducido=int(input("Introduce tamaño 1 o 2: "))
cantidadKilos=int(input("Introduce la cantidad en kg: "))

precio=5
if tipoIntroducido.upper()=="A":
    if tamañoIntroducido==1:
        precio+=0.20
    elif tamañoIntroducido==2:
        precio+=0.30
elif tipoIntroducido.upper()=="B":
    if tamañoIntroducido==1:
        precio-=0.3
    elif tamañoIntroducido==2:
        precio-=0.5
precio*=cantidadKilos
print(precio," euros")
