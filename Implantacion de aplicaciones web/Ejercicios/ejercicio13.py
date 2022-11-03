#pedir
mes=int(input("Introduce un mes entre 1 y 12: "))
dia=int(input("Introduce un dia del mes: "))

year=int(input("Introduce un año: "))


if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    if dia<=31:
        print("FECHA CORRECTA!")
elif mes==4 or mes==6 or mes==9 or mes==11:
    if dia<=30:
        print("FECHA CORRECTA!")
elif mes==2:
    if dia<=28:
        print("LA FECHA ES CORRECTA!")
    elif dia==29 and (year%4==0 and year%100!=0 or year%400==0 ):
        print("FECHA CORRECTA AÑO BISIESTO!")
                
else: 
    print("FECHA INCORRECTA")
