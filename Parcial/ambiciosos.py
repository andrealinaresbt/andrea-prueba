#1

def get_divisores(number, divisores_num): #esto te da los divisores de un numero
    aux = 0
    while aux < number:
        aux +=1
        if number%aux == 0:
            divisores_num.append(aux) 
            
    divisores_num.pop(-1)
    return divisores_num
        
def get_divisores2(suma_divisores_ambi, divisoresaux):
    aux = 0
    while aux < suma_divisores_ambi:
        aux +=1
        if suma_divisores_ambi%aux == 0:
            divisoresaux.append(aux) 

    divisoresaux.pop(-1)
    return divisoresaux





        
def main():
    divisores_num= []
    divisoresaux= []
    while True:
        number = int(input('please enter a natural number: '))
        if number <= 0 :
            print("This is not a natural number nor an ambicious number, try again.")
        else:
            divisores_num = get_divisores(number, divisores_num)
            suma_divisores_ambi= sum(divisores_num)
            divisores_aux= get_divisores2(suma_divisores_ambi,divisoresaux)
            suma_aux = sum(divisores_aux)
            if suma_divisores_ambi == suma_aux:
               print(f'{number} is an ambicious number')
            else:
                print(f'{number} is  not an ambicious number')
            option = input('Do you want to continue? \n Y-Yes. \n N-No. \n ---> ').upper()
            if option == 'N':
                print('******************* GOODBYE *******************')
                break

main()