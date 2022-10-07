def main():
    
    n = 0
    aux = 0
    num = (input('please enter a number: '))

    
    if num.isnumeric:
        num = int(num)
        if num > 1:
            for i in range(2,num):
                if num%i == 0:
                    print(f'{num} is not a fermant prime number')
                    break

                
                elif num == 1:
                    print(f'{num} is not a fermant prime number')
                    
                else:
                    while n < num:
                        operacion = (2**2**n) + 1
                        if operacion == num:
                            aux += 1
                        n += 1

            if aux == 1:
                 print(f'{num} is a fermant prime number')

        if aux != 1:
            print(f'{num} is not a fermant prime number')
            

        

        

            

    
    else:
        print('please enter a valid number')

            



      
main()