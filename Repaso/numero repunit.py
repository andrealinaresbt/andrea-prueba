num = input('please enter a number: ')
Strnum = str(num)
primero = str(num)[0]

sumDigitos= 0

rep = True
for i in str(num):
    sumDigitos += int(i)  
    if primero != i:
     rep = False


            
if rep == False:
    print(f'the number {Strnum} is not repunit')

else:
    print(f'the number {Strnum} is repunit')

cuadrado = False
for j in range(2, sumDigitos):
    if j**2 == sumDigitos:
        cuadrado = True
        break
if cuadrado == False:
    print(f'the number {sumDigitos} is not square')
else:
    print(f'the number {sumDigitos} is square')   
    


       
      