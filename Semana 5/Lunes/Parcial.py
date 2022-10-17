from http import client


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
    print('NetAmount:', client.get('study'))


    



def main():
    studied_dic = {'U':
    {'name': 'Ultrasonido' , 'price': '8900'} ,
    'T':{'name': 'Tomografia' , 'price': '12640'},
    'R':{'name': 'Resonancia' , 'price': '16500'} }
    clients=[]
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
                




                print_invoice(client)
                clients.append(client)
            if option_menus == 2:
                print('*******GOODBYE********')
                break
            
    
        
    

            

    



main()