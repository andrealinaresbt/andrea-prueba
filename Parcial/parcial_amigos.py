def welcome():
    print('---------- WELCOME --------------')

def get_divisores(num1, divisores_num1): #esto te da los divisores de un numero
    aux = 0
    while aux < num1:
        aux +=1
        if num1%aux == 0:
            divisores_num1.append(aux) 
        

    divisores_num1.pop(-1)
    return divisores_num1
            
def get_divisores2(num2, divisores_num2): #esto te da los divisores de un numero
    aux = 0
    while aux < num2:
        aux +=1
        if num2%aux == 0:
            divisores_num2.append(aux) 

    divisores_num2.pop(-1)
    return divisores_num2

def main():
    welcome()
    
    while True:
        divisores_num1 = []
        divisores_num2=[]
        num1 = int(input('Please enter one number: '))
        num2= int(input('please enter a second number: '))
        get_divisores(num1, divisores_num1)
        sum1 = sum(divisores_num1)
    
        get_divisores2(num2, divisores_num2)
        sum2 = sum(divisores_num2)
        if sum1 != num2 and sum2 != num1:
            print('los numeros no son amigos')
            option= input('do you want to try again? \n N-No \ Y-Yes \n -----> ').upper()
            if option == 'N':
                break
        else:
            print('los numeros son amigos')

            break
            




main()          

