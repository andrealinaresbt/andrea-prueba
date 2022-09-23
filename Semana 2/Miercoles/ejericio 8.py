number= int(input('please enter a number '))
aux= number -1
cont=0

if number ==1:
    print(f'The number {number} isnt prime')

else:
    while aux > 2:
        if number % aux == 0:
            cont =+ 1
            break
        aux -= 1

if cont == 0:
    print(f'the number {number} is prime')
else:
    print(f'the number {number} isnt prime')
    #recordar y repasar
    