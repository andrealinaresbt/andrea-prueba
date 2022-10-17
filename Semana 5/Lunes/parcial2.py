def greetings():
    print('**********WELCOME************ \n')

def view_delivery(delivery):
    for places,price in delivery.items():
        print(f'{places} ---> {price}' + '$')

def view_menu(menu):
    for things in menu:
        lista_ingredientes = list(ingrediente for ingrediente in things["ingredientes"]) #Para que como sirve

        ingredientes = ", ".join(lista_ingredientes)
       
        print(f"""Nombre: {things['pizza']}
    Ingredientes: {ingredientes}
    Tipo de precio según tipo de cocinado:
    --->Parrilla: {things["precio"]["a la parrilla"]}
    --->Leña: {things["precio"]["a la leña"]}
        """)
   #solo funciona con '''   
def orden(menu, ContadorPizza, ContadorTamano):
    pizza_options = {'Margarita': 1,
     "Pepperoni": 2, 
    "4 Estaciones": 3, 
    "Prosciutto Funghi": 4, 
    "Española": 5}
    while True:
        pizza_option = (input('''please enter the name of the pizza option you would like:
        - Margarita.
        - Pepperoni 
        - cuatro Estaciones
        - Prosciutto Funghi
        - Española
        ----> ''')).capitalize().strip()
        
        
        if pizza_option not in list(pizzadic["pizza"] for pizzadic in menu):
            print('this flavor is not available. try again')
            
        
        else: 
            cocina_opcion = int((input('please enter how you would like your pizza: \n1. A la parrilla. \n2. A la leña ---->  ')))

            if cocina_opcion == 1:
                tipo = 'a la parrilla'
            elif cocina_opcion == 2:
                tipo = 'a la leña'
            else:
                print('please enter a valid value')

            amount = 0
            for pizza_options in menu:
                if pizza_options['pizza'] == pizza_option:
                    costo = int(pizza_options["precio"][tipo][:-1])

            tamaño_choice = [8,10,12]
            pick_tamano = input('please enter the option of pizza size you want to buy' +f' {tamaño_choice} --->')
            if pick_tamano.isnumeric():
                pick_tamano= int(pick_tamano)
                if pick_tamano not in tamaño_choice:
                    raise Exception
                if pick_tamano == 8:
                    costo += 0
                elif pick_tamano == 10:
                    costo += 5
                else:
                    costo+= 10

            
                cantidad = int(input('how many pizzas do you want?  '))
                costo = cantidad*costo
                ContadorPizza[pizza_option]+= cantidad
                ContadorTamano[pick_tamano] += cantidad
                    

                
                
                return pizza_option, costo, tipo, cantidad, pick_tamano
            else:
                ('please try again')

        break

def prime_number(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        
        elif num == 1:
            return False
            
        else:
           return True

def cedula():
    while True:
        try:
            client_id= input('please enter your id: ')
            number_needed = int(client_id[:-1])
            if prime_number(number_needed) == True:
                descuento = 0.05
            else:
                descuento = 1
            return client_id, descuento
        except:
            print('please enter a valid value')

def name():
    while True:
        try:
            name = input('please enter your name: ') #preguntar como hacer que no explote si le pregunto el apellido
            if not (name.isalpha()):
                print('This is not your name.')
                raise Exception
            return name
        except: 
            print('-----This is not  valid answer. Try again.-----')
                

def payment():

    payment_list = ['Debito', 'Efectivo', 'Zelle']
    while True:
        try:
            payment_method= input('please enter your payment method: Debito, Efectivo or Zelle:  ').strip().capitalize()
            if payment_method not in payment_list:
                print('This was not a valid payment method. Pick a valid option.')
                raise Exception
        except:
            print('Please try again')
    
        return payment_method

def pedido_information():
    client_name = name()
    payment_method = payment()
    client_id, descuento = cedula()
    return client_name, payment_method, client_id, descuento

def compra(menu, delivery, ContadorPizza, ContadorTamano, ListaDePizza, ListaDePedidos, ContadorID, ContadorMunicipio):
    client_name, payment_method, client_id, descuento = pedido_information()
    delivery_add = 0
    if ListaDePizza.get(pizza_option) == None:
        ListaDePizza[pizza_option] = {"Price": {costo}, "Size": {pick_tamano}, "'Cantidad'": {cantidad}}
        ListaDePedidos[ContadorID] = { "Nombre": client_name, "Cedula": client_id, "Forma de Pago": payment_method, 
    "CantidadPizas": cantidad,
    "Tamaño": pick_tamano,
    "Tipo de cocinado": tipo,
    "Costo": costo,
    "Delivery": delivery_add,
    "Descuento": descuento}
    while True:
        view_menu(menu)
        pizza_option, costo, tipo, cantidad, pick_tamano = orden(menu, ContadorPizza, ContadorTamano)
        quantity = (input('do you want to buy another pizza?: \n Y-Yes \n N-No \n --->')).upper()
        

        
        if quantity == 'Y':

            ContadorID += 1
        
            
            
        elif quantity == 'N':
            delivery_add = finish_compra(delivery, ContadorMunicipio, ListaDePedidos, ListaDePizza)
    
         #preguntar como hacer para poner una condicion que me permita ir acumulando los pedidos de pizza
            return pick_tamano, ListaDePedidos, ContadorTamano, ContadorMunicipio, delivery_add
            
        

        else:
            print('Please select a valid answer')
            break

    
    




    

    

    
        
        
            

       

def finish_compra(delivery, ContadorMunicipio, ListaDePedidos, ListaDePizza):
    while True:
        costo2= 0

        retire_option = int(input('how would you like to get ur food? \n1. Delivery (additional Cost). \n2. Pick-Up. \n ----> '))
        if retire_option == 1:
            while True:
                
                view_delivery(delivery)
                municipio_pick = input('please enter the name of the municipe you want the delivery to be:  ').strip().capitalize()
                if municipio_pick not in delivery.keys():
                    print('--------- This is not a valid option. Try again. -------')
            
                else:
                    ContadorMunicipio[municipio_pick]+= 1
                    delivery_add = (delivery[municipio_pick])
            
                    return delivery_add
                break
                        

        elif retire_option ==2:
            delivery = 0
            break

        else:
            print('----- This is not a valid option. Please pick a valid delivery option -----')
            break

        break
                    

def main():
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
    
    delivery = {

   "Chacao":2,

   "Sucre":3,

   "Baruta":4,

   "El Hatillo":4,

   "Carrizal":4

}
    
    ContadorPizza = {'Margarita': 0,
     "Pepperoni": 0, 
    "4 Estacioens": 0, 
    "Prosciutto Funghi": 0, 
    "Española": 0}
    ContadorTamano = {8:0, 10:0 ,12:0}
    ContadorMunicipio = {"Chacao":0, "Sucre":0, "Baruta":0, "El Hatillo":0, "Carrizal":0}
    ContadorID = 0

    ListaDePizza={}
    ListaDePedidos = {}
    location= None

    greetings()
    while True:
        
        ContadorID=0
        ContadorID += 1
        option = input('Please enter an option: \n1. View Menu. \n2. Make a Purchase. \n3. Exit. \n ----->')

        if option.isnumeric():
            option = int(option)
            try:
                if option == 1:
                    view_menu(menu)

                elif option == 2:
                    
                    
                    compra(menu, delivery, ContadorPizza, ContadorTamano, ListaDePizza, ListaDePedidos, ContadorID, ContadorMunicipio)
                   

                    print(ListaDePedidos)
                   

            except:
                print('something went wrong with the process')
                raise Exception



                


                if option == 3:
                    break





    
main()