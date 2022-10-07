
#para buscar un elemento de un diccionario dentro diccionario, solamente sigues agregando a .get

#para tener un solo elemento de una lista en un diccionario "elementos1.get(p
def main():
    num1= int(input('please enter a number '))
    num2 = int(input('please enter a second number '))
    aux = num1 -1
    aux2= num2 -1
    acum = 0
    acum2= 0

    while aux >= 1:
        if num1 % aux == 0:
            acum += aux
        aux -= 1
        #esto calcula divisores

    while aux >= 1:
        if num2 % aux2 == 0:
            acum2 += aux2
        aux2 -= 1
        #esto calcula divisores
   

    if acum == acum2:
        print('the numbers are friends')
    else:
        print ('the numbers are not friends')
   
    

main()