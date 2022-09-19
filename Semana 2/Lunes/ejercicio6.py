num1=(input('Please enter a number '))

if num1.isnumeric():
    num1 = int(num1)

if num1%2 == 0:
    print(f'{num1} es par')
else:
    print(f'{num1} es impar')
