def get_primes(num):
    primes = []
    lisst= []
    jola=[]
    for n in range(0, num+1):
        contador = 0
        for i in range(1,n+1):
            if n % i == 0:
                contador += 1
        if contador == 2:
            primes.append(n)
            while len(primes) >=2 and len(primes) < num:
                jola2 = primes[-1]*primes[-2]
                
                jola.append(jola2)
                break

    
    return primes, jola
def main():
    num = int(input('please enter a number: '))
    
    primes, lista_num = get_primes(num)

    if num in lista_num:
        print('You found the numbers')
    else:
        print("They dont exist")
    

    




main()