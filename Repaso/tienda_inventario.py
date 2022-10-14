from itertools import product


def main():
    print('**welcome to our store**')
    
    products = {
    "mobiles": {
        "Apple": [
            {
                "id": 1,
                "name": "iPhone 7",
                "price": 300
            },
            {
                "id": 2,
                "name": "iPhone 8",
                "price": 350
            },
            {
                "id": 3,
                "name": "iPhone Xr",
                "price": 450
            },
            {
                "id": 4,
                "name": "iPhone Xs",
                "price": 460
            },
            {
                "id": 5,
                "name": "iPhone 11",
                "price": 900
            },
            {
                "id": 6,
                "name": "iPhone 12",
                "price": 1100
            },
            {
                "id": 7,
                "name": "iPhone 13",
                "price": 1300
            },
        ],
        "Samsung": [
            {
                "id": 8,
                "name": "Samsung Galaxy Beam",
                "price": 150
            },
            {
                "id": 9,
                "name": "Samsung Galaxy S6",
                "price": 200
            },
            {
                "id": 10,
                "name": "Samsung Galaxy S7",
                "price": 300
            },
        ],
        "Xiaomi": [
            {
                "id": 11,
                "name": "Xiaomi Redmi Note 8",
                "price": 250
            },
            {
                "id": 12,
                "name": "Xiaomi Redmi Note 8 Pro",
                "price": 300
            },
        ]
    },
    "laptops": {
        "DELL": [
            {
                "id": 13,
                "name": "Dell Inspiron 15",
                "price": 600
            },
            {
                "id": 14,
                "name": "Dell Latitude 14",
                "price": 650
            },
        ],
        "MAC": [
            {
                "id": 15,
                "name": "MacBook Pro 13",
                "price": 900
            },
            {
                "id": 16,
                "name": "MacBook M1",
                "price": 1500
            },
        ]
    },
}
    while True:
        option= input('What can we help you in today? \n 1- View inventory. \n 2- Make a purchase. \n 3- Exit. ')
        if option.isnumeric:
            option = int(option)
            if option == 1:
                for types,brand in products.items():
                    for brand_name, product_list in brand.items():
                        print(brand_name)
                        for product in product_list:
                            id = product.get('id')
                            name = product.get('name')
                            price = product.get('price')
                            print(f'\n {id} \n name --> {name} \n price --> {price}' )

            elif option == 2:
                client_information= {}
                name_client= input('what is your name? ')
                id_client= input('what is your id? ')
                id_buy = int(input('what is the product id you wish to purchase? '))
                client_information['name'] = name_client
                client_information['id'] = id_client
                client_information['purchase'] = id_buy

                product_purchased= None

                for types,brand in products.items():
                    for brand_name, product_list in brand.items():
                        for product in product_list:
                            #esto imprime por producto print ('*****receip******') 
                            if product.get('id') == id_buy:
                                product_purchased = product
                                break
                if product_purchased == None:
                    print('product not found')
                
                else:
                    print('****receip*****')
                    for key,value in client_information.items():
                       print(key,value)
                    for key,value in product_purchased.items():
                        print(key,value)
                       

                
                    

                     
                    

            else:
                print('Thank you for coming')
                break
                                    

                
                
               
                                
                                
                                        





main()