from sre_compile import isstring


num = (input('please enter a number: '))
if num.isnumeric:
    num = int(num)
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                print(f'{num} is not a prime number')
            
    elif num == 1:
        print(f'{num} is not a prime number')
    else:
        print(f'{num} is a prime number')
  
else:
    print('please enter a valid number')
