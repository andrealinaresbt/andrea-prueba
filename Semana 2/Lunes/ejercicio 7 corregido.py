print('Hello welcome to Bella Napoli')
option = input('please enter an option: \n\t1 - Vegetarian \n\t2 -Non Vegetarian ')
option== True

if option.isnumeric():
    option=int(option)
    if option == 1:
        ingredient= input('please pick one topping only: \n\t1- Pimiento \n\t2- Tofu ')
        if ingredient== '1' :
            ingredient= "pimiento"
        elif ingredient== '2':
              ingredient= 'tofu'
              print(f'La pizza vegetariana con {ingredient} ')
    if option == 2:
        ingredient= input('please pick one topping only: \n\t1- Pepperoni \n\t2- Jamon \n\t3- Salmon ')
        if ingredient== '1' :
            ingredient= "pepperoni"
        elif ingredient== '2':
              ingredient= 'jamon'
        else:
            ingredient = 'salmon'
    else:
        print('Not valid option')
    print(f'La pizza normal con {ingredient}')
              