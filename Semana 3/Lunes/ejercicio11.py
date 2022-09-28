number = input('Please enter a number: ')

if number.isnumeric():
    number = int(number)
    number = number+1
    for index in range (1, number):
        print("*"*index)

else:
    print('error')
