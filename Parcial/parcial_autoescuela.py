def welcome():
    print('------------------------- W E L C O M E ----------------------')
    print('This is La Rapida Autoschool!')

def get_client_info(driving_dic):
    while True:
        for key, value in driving_dic.items():
            print(f'----> {key} <----')
            for key_internos, value_internos in value.items():
                print(f'{value_internos}')
            print('')
        client_car = input('Please enter the first letter of your car option:').upper()
        if client_car == 'S' or client_car == 'A':
           return client_car
           break
        else:
            print('this is not a valid value')
        

        

def client_information(client_car):

    client = {
        'id': input('please enter the client ID: '),
        'hours': int(input('please enter the client hour time: ')),
        'type of car': client_car 
        }
    return client

def descuento_get(client, gross_amount, discount_counter):
    if client.get('hours') >= 3:
        descuento = 0.15*gross_amount
        discount_counter += 1
        return descuento, discount_counter

def print_invoice(driving_dic, total_amount, client, client_car):
    print('\n----------INVOICE---------')
    print(f' ID: {client.get("id")} \n Type of vehicle: {driving_dic.get(client_car).get("name")} \n Total amount: {total_amount} \n')


def main():
    welcome()
    driving_dic = {'A':
    {'name': 'Automatico' , 'price per hour': 2500} ,
    'S':{'name': 'Sincronico' , 'price per hour': 3500},
    }
    clients=[]
    descuento = 0
    client_count = 0
    client_a= 0
    client_b =0
    discount_counter = 0
    total_day =0

    while True:
        print('Are you ready?')
        client_car = None
        drive_picked = None
        client_count +=1
        client_car = get_client_info(driving_dic)
        client = client_information(client_car)
        clients.append(client)
        gross_amount = driving_dic.get(client_car).get('price per hour')
        descuento, discount_counter = descuento_get(client, gross_amount, discount_counter)
        total_amount = gross_amount - descuento
        total_day += total_amount
        print_invoice(driving_dic, total_amount, client, client_car)

   


        option1=input('Do you want to see today final stats? \n Y-Yes. \n N-No. \n ----->').upper()
        
        if option1 == 'Y':
            print('----------END OF THE DAY-------------')
            print(f'The total amount of clients today were of {client_count}')
            if client_car == 'S':
                client_b +=1
            if client_car == 'A':
                client_a +=1
            
            promedio_total= total_day/client_count
            print(f'The total amount of clients for Automatic cars was of {client_a}')
            print(f'The total amount of clients for Synchronic cars was of {client_b}')
            print(f'The total amount of clients who got a discount was of {discount_counter}')
            print(f'The total amount of clients who got a discount was of {promedio_total}')
            break
        

            





            



main()