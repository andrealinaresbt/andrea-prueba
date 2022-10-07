def main ():

    print('Hello this is the main option menu')
    infraction={
        1:{"name":"Choque", "cost":50},
        2:{"name":"Semáforo", "cost":30},
        3:{"name":"Falta de documentos", "cost":100},
    }

    officers={
        1:{"name":"Luis", "lastName":"Bello","ci":13452224},
        2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
        3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
    }

    db={}
    
    print(officers)
    

        

    list_of_infractors =[]
    infraction_done = None
    while True:
        
        option = input('please enter an option: \n 1. Register infraction data. \n 2. Remove infraction data. \n 3. Show all the infractions. \n 4. Exit. ')    
        if option.isnumeric():
            option = int(option)
            if option == 1:
                infractor_information= {}
                name_infractor= input('what is your name? ')
                id_infractor= input('what is your id? ')
                infraction_type = int(input('what is the number of the infracion you commited: \n 1. Choque. \n 2. Semaforo. \n 3. Falta de documentacion   '))
                officer_number = int(input('what is the number of the officer who is writing the report  '))
                infractor_information['name'] = name_infractor
                infractor_information['id'] = id_infractor
                infractor_information['infraction'] = infraction_type
                infractor_information['police officer'] = officer_number

                list_of_infractors.append(infractor_information)
                
                for names,officer in officers.items():
                    for officer_number, number_assigned in officer.items()
                        if officer_number == officer.get('name')
                        officer_picked = officer
                        break
                
                print(officer_picked)


            


    
                
        if option == 4:
            break
            
            





main()