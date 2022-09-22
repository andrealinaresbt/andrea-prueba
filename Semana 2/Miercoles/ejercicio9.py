number =int(input('please enter a number '))
aux = number -1
acum = 0

while aux >= 1:
    if number % aux == 0:
        acum += aux
    aux -= 1

if number < acum:
    print(f'the number {number} is abundant')
else:
     print(f'the number {number} is not abundant')
