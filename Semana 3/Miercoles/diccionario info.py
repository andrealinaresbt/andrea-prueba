informacion = {}

while True:
    data_key= input('Please enter what data you want to save: ')
    data_value= input('Please enter the value you want to save: ')
    informacion[data_key] = data_value
    print('Your data is:')

    for key, value in informacion.items():
        print(f'Your {key} is {value} ')

    if input('do you want to exist? \n Y-Yes \n N-No  ') == 'Y':
        break


    