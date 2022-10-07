#ANDREA LINARES 30496934


def main ():
   
    print('******WELCOME TO Saman-Labs******')
    medications = {
            "prescription": {
                "antibiotics": {
                    "skin": [
                        {
                            "id": 1,
                            "name": "Clindamicine",
                            "price": 300
                        },
                        {
                            "id": 2,
                            "name": "Cefadroxil",
                            "price": 350
                        },
                        {
                            "id": 3,
                            "name": "Amoxicillin",
                            "price": 320
                        }
                    ],
                    "respiratory-system":[
                        {
                            "id": 4,
                            "name": "Citromicine",
                            "price": 380
                        },
                        {
                            "id": 5,
                            "name": "Levofloxacine",
                            "price": 125
                        },
                        {
                            "id": 6,
                            "name": "Azitromicine",
                            "price": 740
                        }
                    ]
                },
                "analgesic": {
                    "anti-inflammatories": [
                        {
                            "id": 7,
                            "name": "HYDROCODONE-IBUPROFEN",
                            "price": 150
                        },
                        {
                            "id": 8,
                            "name": "IBUDONE",
                            "price": 180
                        }
                    ]
                }
            },
            "non-prescription": {
                "analgesic": {
                    "general": [
                        {
                            "id": 9,
                            "name": "Acetaminophen",
                            "price": 15
                        },
                        {
                            "id": 10,
                            "name": "Ibuprofen",
                            "price": 20
                        }
                    ]
                },
                "antihistamine": {
                    "antiallergic": [
                        {
                            "id": 11,
                            "name": "Loratadine",
                            "price": 12
                        },
                        {
                            "id": 12,
                            "name": "Desler M",
                            "price": 8
                        },
                        {
                            "id": 13,
                            "name": "Allegra",
                            "price": 21
                        },
                        {
                            "id": 14,
                            "name": "Fexofenadine",
                            "price": 18
                        }
                    ]
                }
            }
        }


    while True:
       option= input('What can we help you in today? \n 1- View inventory. \n 2- Make a purchase. \n 3- Exit. ')
       if option.isnumeric:
            option = int(option)
            if option == 1:
                for types,brand in medications.items():
                    
                    for brand_name, medication_list in brand.items():

                        for med, medicine in medication_list.items():
                           
                            for key  in medicine:
                                id = key.get('id')
                                name = key.get('name')
                                price = key.get('price')
                                print(f' Your product is {types}, {brand_name} and {med} \n  {id} \n name --> {name} \n price --> {price}' )
                                
                            
                            
                        

            if option == 2:
                client_information= {}
                name_client= input('what is your name? ')
                id_client= input('what is your id? ')
                id_buy = int(input('what is the product id you wish to purchase? '))
                client_information['name'] = name_client
                client_information['id'] = id_client
                client_information['purchase'] = id_buy

                product_purchased= None

                for types,brand in medications.items(): 
                    
                    for brand_name, medication_list in brand.items():

                        for med, medicine in medication_list.items():
                            for key  in medicine:
                                if key.get('id') == id_buy:
                                    product_purchased = medications
                                    break

                if product_purchased == None:
                    print("pick another option")
                    
                else:
                    print('****receip*****')
                    for hrllo,hi in client_information.items():
                       print(hrllo, hi)
                       for key,value in product_purchased.items():
                        for key  in medicine:
                                id = key.get('id')
                                name = key.get('name')
                                price = key.get('price')
                                break
            
                    print(f' Your product is {types}, {brand_name} and {med} \n  {id} \n name --> {name} \n price --> {price}' )
                                
                        
                

            if option == 3:
                print('thank you for coming')
                break
        
                

                
                    



                                        

                                        
                                        
                                        
                                                

                                
                                        

                            
                        
                            
                           
            

main()