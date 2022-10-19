def fibonacci(num):
    i = [0,1]
    while i[-1] < num:
        i.append(i[-1]+i[-2]) #agrega el ultimo numero agregado en la lista con el numero anterior al mismo
    return i
    
def main():
    bionacci_list =[]
    while True: 
        number = int(input('Enter the number you want to check:  '))
        if number < 0:
            print('This is not a fibonacci number. Please only enter natural numbers. ')
            break
        else:
            lista= fibonacci(number)
            if number in lista:
                print(f'{number} is a fibonacci number')
            else:
                print(f'{number} is not a fibonacci number')

        


main()