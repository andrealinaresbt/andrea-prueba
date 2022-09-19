number_one = (input('Please enter a number '))
number_two = (input('Please enter a second number '))
is_valid= True
if number_one.isnumeric():
    number_one= float(number_one)
else:
    is_valid= False

if number_two.isnumeric():
    number_two= float(number_two)
else:
    is_valid= False
if is_valid:
    if number_two==0:
        print('Error')
    else:
        print(number_one/number_two)
else:
    print('Error')

 