number = (input('Please enter a number '))
aux = 1
if number.isnumeric():
    number = int(number)
    while aux < number:
        if aux + 2  <= number:
            print(aux)
        else:
            print(aux, end= ',')

        aux+=2
        # el aux +=2 nos quita los numeros pares
else:
    print('Error in data, try again')


