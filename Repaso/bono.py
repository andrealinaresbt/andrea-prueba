
def PedirPizza(menu, TiposPizzaPedidas, CantidadTamanoPedidas):
    pizzasEnMenu = {"Margarita": 0, "Pepperoni": 1, "4 Estacioens": 2, "Prosciutto Funghi": 3, "Española": 4}
  
    while True:        
        try:
            pizza = input("Ingrese el nombre de la pizza que desea: ").strip().capitalize()

            if pizza not in list(pizza["pizza"] for pizza in menu):
                raise Exception

            tipoNum =  int(input("""Ingrese el número del tipo de la pizza que desea: 
1. Parrilla
2. A la leña 
>"""))

            if not (tipoNum == 1 or tipoNum == 2):
                raise Exception
            else:
                if tipoNum == 1:
                    tipo = "a la parrilla"
                elif tipoNum == 2:
                    tipo = "a la leña"

            costo = 0
            for pizzaDic in menu:
              if pizzaDic["pizza"] == pizza:
                costo = int(pizzaDic["precio"][tipo][:-1])
          

            tamanosPermitidos = [8, 10, 12]
            tamano =  int(input("Ingrese el tamaño de la pizza que desea (8, 10, 12): "))

            if tamano not in tamanosPermitidos:
                raise Exception

            if tamano == 8:
                costo += 0
            elif tamano == 10:
                costo += 5
            elif tamano == 12:
                costo += 10

            cantidad =  int(input("Ingrese la cantidad de pizzas que desea: "))

            costo = costo*cantidad

            TiposPizzaPedidas[pizza]+= 1
            CantidadTamanoPedidas[tamano] += 1
          
            return pizza, tipo, costo, tamano, cantidad
        except:
            print("Algo salió mal con su pedido, vuélvalo a intentar")


def MostrarPizzas(menu):
    print("Por favor escoja su pizza: \n")
    for pizza in menu:
        ingredientesList = list(ingrediente for ingrediente in pizza["ingredientes"])
        ingredientes = ", ".join(ingredientesList)
        print(f"""Nombre: {pizza['pizza']}
    Ingredientes: {ingredientes}
    Tipo de precio según tipo de cocinado:
        A la Parrilla: {pizza["precio"]["a la parrilla"]}
        A la Leña: {pizza["precio"]["a la leña"]}
        """)


def FormatoPago():
    while True:
        formatos = ["Debito", "Zelle", "Efectivo"]
        try:
            formato = input("Ingrese su formato de pago por favor: ").strip().capitalize()
            
            if formato not in formatos:
                raise Exception

            return formato
        except:
            print("Ingrese un valor válido")


def EsPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



def Cedula():
    while True:
        try:
            descuento = 1            
            cedula = input("Ingrese su cédula por favor: ")
            
            if EsPrimo(int(cedula[-1])):
                descuento = 0.95

            return cedula, descuento
        except:
            print("Ingrese un valor válido")



def Nombre():
    while True:
        try:            
            nombre = input("Ingrese su nombre por favor: ")
            
            if not (nombre.isalpha()):
                raise Exception

            return nombre
        except:
            print("Ingrese un valor válido")

def PedirDatos():
    cedula, descuento = Cedula()
    nombre = Nombre()
    formatoPago = FormatoPago()

    return nombre, cedula, descuento, formatoPago


def ComprarPizza(menu, delivery, pedidos, idPedidos, pedidosMunicipios, TiposPizzaPedidas, CantidadTamanoPedidas, listaPizzas):
    
    nombre, cedula, descuento, formatoPago = PedirDatos()
    while True:
        MostrarPizzas(menu)
      
        pizza, tipo, costo, tamano, cantidad = PedirPizza(menu, TiposPizzaPedidas, CantidadTamanoPedidas)
        
        if listaPizzas.get(pizza) == None:
            listaPizzas[pizza] = {"Precio": {costo}, "Tamaño": {tamano}, "Cantidad": {cantidad}}
        
        pedidos[idPedidos] = {
        "Nombre": nombre, 
        "Cedula": cedula, 
        "FormatoPago": formatoPago, 
        "CantidadPizas": cantidad,
        "Tamaño": tamano,
        "Tipo de cocinado": tipo,
        "Costo": costo,
        "DelivieryExtra": 0,
        "Descuento": descuento}

        try:
            opcion = int(input("""Desea comprar otra pizza o finalizar la compra?
    1. Comprar otra piza
    2. Finalizar Compra
>"""))
            if opcion == 2:
                return pedidos, pedidosMunicipios, TiposPizzaPedidas, CantidadTamanoPedidas
            elif opcion == 1:
                idPedidos += 1
            else:
                raise Exception

        except:
            print("Ingrese un valor válido por favor:")

def CerrarCompra(delivery, pedidos, pedidosMunicipios, listaPizzas):
    while True:
        for pedido in pedidos:
            print(pedido)
            try:
                deliverOPickUp = int(input("""Cómo le gustaría recibir su pedido?
            1. Delivery
            2. Pick Up
        >"""))

                if deliverOPickUp == 1:
                    while True:
                        try:
                            municipio = input("Ingrese el municipio donde desea recibir sus pizzas: ").strip().Capitalize()

                            if municipio not in delivery.keys():
                                raise Exception
                            else:
                                pedido["DelivieryExtra"] += delivery[municipio]
                                pedidosMunicipios[municipio] += 1
                                break
                        except:
                            print("Ingrese un municipio válido")
                elif deliverOPickUp == 2:
                    pass
                else:
                    raise Exception
            except:
                print("Ingrese un valor válido por favor:")
            
            print(f"""
            Nombre: {pedido["Nombre"]}
            Cedula: {pedido["Cedula"]}
            FormatoPago: {pedido["FormatoPago"]}
            """)

            for nombre, datos in listaPizzas.items():
                print(f"""Tipo de piza: {nombre}:
            Precio: {datos["Precio"]}
            Tamaño: {datos["Tamaño"]}
            Cantidad: {datos["Cantidad"]}""")

            costo = pedido["Costo"]
            print(f"Precio sin delivery: {costo}")

            if pedido["DelivieryExtra"] != 0:
                costo += pedido["DelivieryExtra"] 
                print(f"Precio con delivery: {costo}")

            if pedido["Descuento"] != 0:
                costo *= pedido["Descuento"]
                print(f"Precio con descuento: {costo}")
            break

def main():
    delivery = {
    "Chacao":2,
    "Sucre":3,
    "Baruta":4,
    "El Hatillo":4,
    "Carrizal":4}

    listaPizzas = {}

    pedidos = {}

    TiposPizzaPedidas = {"Margarita": 0, 
    "Pepperoni": 0, 
    "4 Estacioens": 2, 
    "Prosciutto Funghi": 0, 
    "Española": 0}

    CantidadTamanoPedidas = {8: 0,
    10: 0,
    12: 0}

    pedidosMunicipios = {
    "Chacao":0,
    "Sucre":0,
    "Baruta":0,
    "El Hatillo":0,
    "Carrizal":0}

    idPedidos = 0

    menu = [
{

    "pizza":"Margarita",

    "ingredientes":[

        "salsa napolitana",

        "queso mozzarella"

    ],

    "precio":{

        "a la parrilla":"6$",

        "a la leña":"8$"

    }
},

{

    "pizza":"Pepperoni",

    "ingredientes":[

        "salsa napolitana",

        "queso mozzarella",

        "pepperoni"

    ],

    "tipo":"a la parrilla",

    "precio":{

        "a la parrilla":"8$",

        "a la leña":"10$"

    }
},

{

    "pizza":"4 Estaciones",

    "ingredientes":[

        "salsa napolitana",

        "queso mozzarella",

        "jamón",

        "maíz",

        "champiñones",

        "pimentones"

    ],

    "tipo":"a la parrilla",

    "precio":{

        "a la parrilla":"11$",

        "a la leña":"12$"

    }
},

{

    "pizza":"Prosciutto Funghi",

    "ingredientes":[

        "salsa napolitana",

        "queso mozzarella",

        "jamón",

        "champiñones",

        "aceite de oliva"

    ],

    "tipo":"a la parrilla",

    "precio":{

        "a la parrilla":"10$",

        "a la leña":"13$"

    }
},

{

    "pizza":"Española",

    "ingredientes":[

        "salsa napolitana",

        "queso mozzarella",

        "jamón serrano",

        "salchichón picante"

    ],

    "tipo":"a la parrilla",

    "precio":{

        "a la parrilla":"12$",

        "a la leña":"14$"
        }
    }
]

    while True:
        idPedidos += 1
        try:
            opcion = int(input(f"""Escoje una de las opciones:
    1. Comprar pizza
    2. Cerrar Compra
    3. Terminar el programa
> """))
            if opcion==1:
                pedidos, pedidosMunicipios, TiposPizzaPedidas, CantidadTamanoPedidas = ComprarPizza(menu, delivery, pedidos, idPedidos, pedidosMunicipios, TiposPizzaPedidas, CantidadTamanoPedidas, listaPizzas)
            
            elif opcion==2:
                CerrarCompra(delivery, pedidos, pedidosMunicipios, listaPizzas)
           
            elif opcion==3:
                
                print("Cantidad de tipos de pizzas vendidos durante el dia")
                for pizza, cantidad in TiposPizzaPedidas.items():
                    print(f"{pizza}: {cantidad}")

                print("Cantidad de tamaÑos de pizzas vendidos durante el dia")
                for pizza, cantidad in CantidadTamanoPedidas.items():
                    print(f"{pizza}: {cantidad}")

                print("Cantidad de tamaÑos de pizzas vendidos durante el dia")
                for pizza, cantidad in CantidadTamanoPedidas.items():
                    print(f"{pizza}: {cantidad}")

                print("Entregas de pizza por municipio durante el dia")
                for municipio, cantidad in pedidosMunicipios.items():
                    print(f"{municipio}: {cantidad}")

                print("Hasta luego")
                break
            else:   
                raise Exception
        
        except:
            print("Ingrese un valor válido")

main()