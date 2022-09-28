number = (input('Please enter a number '))
aux = 1
if number.isnumeric():
    number = int(number)
    number = number +1
    while aux < number:
        for index in range (1, number):
            print(number * index)

        aux+=2
        # el aux +=2 nos quita los numeros pares
else:
    print('Error in data, try again')

