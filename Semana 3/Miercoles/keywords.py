#key dictionary value, permite almacenar keys con cualquier valor que desees.
# se diferencua con las llaves y :, y se acceden con corchetes
# se agregan usando [] con el elemento en '' y = al valor dado.
# para revisar si una llave esta dentro usamos in, si no esta te devolvera un false.
#.get() devuelve none en caso de que el key no exista en vez de key error


elementos = {'hidrogeno' : 1 , 'helio' : 2 , 'carbon': 3}
print(elementos.get('oxigeno', 'no existe' )) 
#el no existe puede ser cambiable, es decir tu decides cual sera el mensaje que te devuelva.
# SI no le das un segundo parametro te devuelve none

elementos = {'hidrogeno' : 1 , 'helio' : 2 , 'carbon': 3}
for elemento, num_value in elementos.items():
    print('El elemento {} tiene un numero atomico de {}.'.format(elemento, num_value))
#el elemento y num_value no tiene un nombre definido, lo primero que pones es el index y el segundo el value.

#el si compara si dos objetos son el mismo,

list1= []
list2 =[]
list3 = list1

if (list1 is list2): #ESta seria falsa porque no tienen la misma posicion de memoria y el si compara eso
    print('True')
else:
    print('False')

if (list1 is list3): #Esta seria verdad porque list3 refiere a la posicion de memoria.
    print('True')
else: 
    print('False')