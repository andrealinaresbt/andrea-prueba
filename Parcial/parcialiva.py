#learn replace
def is_prime(rif):
    number = int(rif[len(rif)-1])
    cont =0
    aux = number -1
    while number > 1:
        if number % aux == 0:
            return False
        aux -= 1
    return True


def main():
    products = {'Q':
    {'name': 'quimico' , 'price': 1000} ,
    'F':{'name': 'farmaceutico' , 'price': 2500},
    'B':{'name': 'biologico' , 'price': 4500} }
    client_f = 0
    client_q = 0
    client_b = 0
    discount_c = 0
    discount_r = 0
    rif_max = 0
    max_purchase = 0
    total_day = 0
    
    while True:
        rif = input('Please enter your rif:  ')
        type_payment = input('Please enter your payment method: \n C - One Time \n R- Credit \n ----->  ').upper()
        product_code = input('Please enter your the product you want to purchase \n Q - Quimico. \n F - Farmaceutico. \n B - Biologico: \n ----->  ')
        discount = 0
        tax = 0
        gross_amount = products.get(product_code).get('price')
        #discounts
        if type_payment == 'C':
            discount += 0.03*gross_amount
        if gross_amount %2== 0:
            discount += gross_amount*0.02
        if is_prime(rif):
            discount += gross_amount*0.05
        #taxes
        if product_code != 'F':
            tax = gross_amount*0.12
        #total a pagar
        total = gross_amount + tax - discount

        #Final day stats
        if product_code == 'F':
            client_f +=1
        elif product_code == 'Q':
            client_q +=1
        elif product_code == 'B':
            client_b +=1

        if type_payment == 'C':
            discount_c += discount
        if type_payment == 'R':
            discount_r += discount
        
        if total > max_purchase:
            rif_max = rif
            max_purchase = total
        
        total_day += total

        #Factura
        print('----------------------------')
        print('          RECEIP            ')
        print('----------------------------')
        print('Rif', rif)
        print("product:", products.get(product_code).get('name'))
        print('Payment method', type_payment)
        print('Discount:', discount)
        print('Total:', total)

        option_exit=input('do you wan to exit? \nY-Yes. \nN-No. \n----->  ').upper()
        if option_exit == "Y":
            print('******END OF THE DAY*******')
            print("Clients F:", client_f)
            print("Clients B:", client_b)
            print("Clients Q:", client_q)
            print("Discount credit:", discount_r)
            print("Discount one time:", discount_c)
            print("Rif maximum purchase:", rif_max)
            print("Total Day:", total_day)
            break
        

        


main()