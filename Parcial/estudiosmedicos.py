
def print_welcome():
     print('*****WELCOME*****')


def get_user_option(dict):
    for key, value in dict.items():
        print(key)
        for key_internos, value_internos in value.items():
            print(f'----> {value_internos}', end = '')
        print('')
    return input('Please enter an option: ').upper()


        
    
    
    
    



    #preguntar como adjuntar el valor del price a la respuesta que me dan
        
    
    

    


def get_client_data(study):
    client = {
        'id': input('please enter the client name: '),
        'gender': input('please enter the client gender M or F: ').upper(), #.lower
        'age': input('please enter the client age: '),
        'study': study 
        }
        


    return client



def print_invoice(client):
    print('*******RECEIP*******')
    print('id:', client.get('id'))
    print('gender:', client.get('gender'))
    print('age:', client.get('age'))
    print('NetAmount:', client.get('total'))


def get_net_amount(client, carros):
    return  carros.get(client.get('study').get('price'))

def get_discount(client, value, cont):
    discount = 0
    if client.get('gender') == "F" and int(client.get('age')) > 55:
        discount += value*0.25
    elif client.get('gender') == "M" and int(client.get('age')) > 65:
        discount+= value *0.25
    if cont %2 != 0:
        discount += value*0.02
    return discount
        
def main():
    studied_dic = {'U':
    {'name': 'Ultrasonido' , 'price': 8900} ,
    'T':{'name': 'Tomografia' , 'price': 12640},
    'R':{'name': 'Resonancia' , 'price': 16500} }
    clients=[]
    clientU= 0
    clientt =0
    clientr = 0
    total_discounts = 0
    totalday = 0
    total_u =0
    total_t= 0
    total_r = 0

    print_welcome()
    while True:
        print('what do you want to do today?')
        study = None
        study_picked = None
        option_menus = (input('Pick an option: \n1. Make a purchase \n2. Exit   \n   '))
        if option_menus.isnumeric:
            option_menus = int(option_menus)
            if option_menus == 1:
                option = get_user_option(studied_dic)
               


                client= get_client_data(option)
                clients.append(client)
                value = get_net_amount(client, studied_dic)
                discount = get_discount(client, value, len(clients))
                total_discounts += discount #te pide el valor como tal de dinero otorgado como descuento
                total_amount = value - discount
                client['total'] = total_amount
                totalday += total_amount
                if option.upper() == 'U':
                    clientU +=1
                    total_u += total_amount
                if option.upper() == 'T':
                    clientt +=1
                    total_t += total_amount
                if option.upper() == 'R':
                    clientr +=1
                    total_r += total_amount

                print_invoice()

                




                print_invoice(client)
                clients.append(client)
            if option_menus == 2:
                print('clients for U:',  clientU)
                print('clients for U:',  clientt)
                print('clients for U:',  clientr)
                print('total discounts:',  total_discounts)
                print('total day:',  totalday)
                if len(clients) > 0:
                    print('total day:',  totalday/len(clients))
                else:
                    print(0)

                if(clientU > 0):
                    print('total day:',  total_u/len(clientU))

                
                print('*******GOODBYE********')
                break
            
    
        
    

            

    



main()