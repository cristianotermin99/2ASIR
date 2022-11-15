diaSemana=input("Que día de la semana es? ")
tipoCliente=input("Que tipo de cliente es? (normal, vip, carlos, ines o pufo): ")
precioTotal=0
seguir=1
cantidadProducto=0
while seguir==1:
    numeroProducto=0
    precioLapiz=1
    precioPC=1010
    precioCoche=4590
    precioSudadera=50
    precioHamburguesa=15
    if diaSemana.upper()=="LUNES" and tipoCliente.upper()!="PUFO":
        print("Se te aplica un 20% en el primer producto por ser lunes!!!!!")
        precioLapiz=precioLapiz-(precioLapiz*0.2)
            
    elif diaSemana.upper()=="MIERCOLES" and tipoCliente.upper()!="PUFO":
        print("HAY 2X1 EN EL COCHE")
        
    elif diaSemana.upper()=="VIERNES" and tipoCliente.upper()!="PUFO":
        precioLapiz=precioLapiz-(precioLapiz*0.7)
        precioPC=precioPC-(precioPC*0.7)
        precioCoche=precioCoche-(precioCoche*0.7)
        precioSudadera=precioSudadera-(precioSudadera*0.7)
        precioHamburguesa=precioSudadera-(precioHamburguesa*0.7)
    elif diaSemana.upper()=="DOMINGO":
        contadorProductos=2
    elif tipoCliente.upper()=="PUFO":
        precioLapiz=precioLapiz+(precioLapiz*0.5)
        precioPC=precioPC+(precioPC*0.5)
        precioCoche=precioCoche+(precioCoche*0.5)
        precioSudadera=precioSudadera+(precioSudadera*0.5)
        precioHamburguesa=precioSudadera+(precioHamburguesa*0.5)
        print("VAS A PAGAR UN 50% MAS POR SER UN MOROSO")
    elif diaSemana.upper()=="MARTES":
        precioLapiz=precioLapiz+(precioLapiz*0.2)
        precioPC=precioPC+(precioPC*0.2)
        precioCoche=precioCoche+(precioCoche*0.2)
        precioSudadera=precioSudadera+(precioSudadera*0.2)
        precioHamburguesa=precioSudadera+(precioHamburguesa*0.2)
        print("VAS A PAGAR UN 20% MAS POR MARTES DIA DE LOS BORDER LINES")
    
        
    if tipoCliente.upper()=="VIP" or tipoCliente.upper()=="CARLOS" or tipoCliente.upper()=="INES":
            precioLapiz=precioLapiz-(precioLapiz*0.1)
            precioPC=precioPC-(precioPC*0.1)
            precioCoche=precioCoche-(precioCoche*0.1)
            print("PAGAS UN 10% MENOS EN LOS 3 PRIMEROS PRODUCTOS POR SER VIP CARLOS O INES")
    

    print("Introduce 1 si quieres comprar un lapiz por ",precioLapiz," euros ")
    print("Introduce 2 si quieres comprar un pc por ", precioPC, " euros ")
    print("Introduce 3 si quieres comprar un coche por ",precioCoche, " euros")
    print("Introduce 4 si quieres comprar una sudadera por", precioSudadera," euros")
    print("Introduce 5 si quieres comprar una burger por ",precioHamburguesa, " euros")
    numeroProducto=int(input("Introduce el numero de producto que desees comprar: "))
    cantidadProducto=int(input("Que cantidad quieres comprar de ese producto: "))   
    if numeroProducto==1:
        precioTotal+=precioLapiz*cantidadProducto
    elif numeroProducto==2:
        precioTotal+=precioPC*cantidadProducto
    elif numeroProducto==3:
        precioTotal+=precioCoche*cantidadProducto
    elif numeroProducto==4:
        precioTotal+=precioSudadera*cantidadProducto
    elif numeroProducto==5:
        precioTotal+=precioHamburguesa*cantidadProducto

    
    seguir=int(input("Quieres seguir compando?: 1. Si  2. No: "))    

print("Precio de tu pedido es: ", precioTotal)
        
        
