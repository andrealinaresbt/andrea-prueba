#No es igual  !=
#Es igual ==

while (True):
    comprar = input('Bienvenidos a mi tienda de zapatos, desea comprar algo?(S/s => Si) \n (N/n => No) ')
    
    if comprar.upper( ) == "S" :
        zapatos = input("""Que zapatos quieres? 
        Tacones 
        Deportivos
        Sandalias 
        Alpargatas """)
        if zapatos.upper( ) == "TACONES":
            pass # SI LLEGA A ACA VA A IGNORAR EL RESTO DE LAS OPCIONES
        elif zapatos.upper( ) == "DEPORTIVOS":
            pass
        elif zapatos.upper( ) == "SANDALIAS":
            pass
        elif zapatos.upper( ) == "ALPARGATAS":
            pass
        break

    elif comprar.upper ( ) == "N" :
        print("Hasta luego")
        break

    else:
        print('Error en el ingreso de datos, intente de nuevo')



