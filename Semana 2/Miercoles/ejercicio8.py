number =int(input('please enter a number '))
aux = number -1
cont =0

if number <= 1 :
      print(f'the number {number} isnt prime')
else:
    while aux >1:
        if number % aux == 0:
        cont +=1
        break
    aux -= 1


if cont == 0:
    print(f'the number {number} is prime')
else:
    print(f'the number {number} isnt prime')


#para ver que pasa ve print en cada parte print('aux', aux) o print('operation', number%aux)