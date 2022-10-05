print('Welcome to Bella Napoli')
option= input('Please enter an option: \n1 - vegetarian\n2 - Non vegetarian\n3 - ->')
if option.isnumeric():
    option=int(option)

if option == 1:
       ingredient = input('please enter an ingrident: \n1- Pimiento\n2 - Tofu\n3 - ->')
       if ingredient == "1" :
        ingredient = "pimiento"
    else:
        ingredient = "tofu"
        print('the pizza is vegetarian and has {ingredient}')

elif option == 2:
       ingredient = input('please enter an ingrident: \n1- Pepperoni\n2 - Jamon\n3 - Salmon')
      if option == 1 
       ingredient = "pepperoni"
     elif:
        ingredient = "jamon"
     else: 
        ingredient= "salmon"
    print('the pizza is non vegetarian and has {ingredient}')

else:
        print('Invalid option')
