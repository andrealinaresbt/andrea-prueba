def welcome():
    print('------------------ WELCOME ---------------------- \n' )

def student_id():
    id_number = input('please enter the number of the students id:  ')

    return id_number

def average_classification(trimestre_uno, trimestre_dos, trimestre_rechazado, cedulas_uno, cedulas_dos, cedulas_reprobado, id_number, grade_average):
    if grade_average >= 18:
        trimestre_uno.append(grade_average)
        cedulas_uno.append(id_number)
        print(f'\nStudent: {id_number} ---- Trimestre Uno \n')
        return trimestre_uno, cedulas_uno

    elif grade_average >= 12 and grade_average <18:
        trimestre_dos.append(grade_average)
        cedulas_dos.append(id_number)
        print(f'Student: {id_number} ---- Trimestre Dos')
        return trimestre_dos, cedulas_dos

    else:
        trimestre_rechazado.append(grade_average)
        cedulas_reprobado.append(id_number)
        print(f'Student: {id_number} ---- Rechazado')
        return trimestre_rechazado, cedulas_reprobado

def main():
    welcome() 
    #almacenan datos
    trimestre_uno = []
    trimestre_dos =[]
    trimestre_rechazado =[]
    cedulas_uno=[]
    cedulas_dos= []
    cedulas_reprobado=[]
    #contador de datos
    aspiring_studentcount = 0
    promedio_uno = 0
    promedio_dos = 0
    promedio_tres = 0
    promedio_total = 0
    suma_de_notas_uno = 0
    suma_de_notas_dos = 0
    suma_de_notas_tres = 0
    

    while True:
        option = int(input('What do you wish to do today?: \n 1. Log Student. \n 2. Show todays record. \n 3. Exit\n ---------->'))
        if option == 1:
            aspiring_studentcount += 1
            name = input('please enter the name of the sudent: ')
            id_number = student_id()
            grade_average = int(input('please enter the students grade average:  '))
            average_classification(trimestre_uno, trimestre_dos, trimestre_rechazado, cedulas_uno, cedulas_dos, cedulas_reprobado, id_number, grade_average)

        elif option == 2:
            print("---------------- F I N A L   D A Y    R E P O R T S --------------")
            #calculos
            if len(trimestre_uno) == 0:
                print('----')
            else:
                suma_de_notas_uno = sum(trimestre_uno)
                promedio_uno = suma_de_notas_uno/(len(trimestre_uno))

            if len(trimestre_dos) == 0:
                print('')
            else:
                suma_de_notas_dos = sum(trimestre_dos)
                promedio_dos = suma_de_notas_dos/(len(trimestre_dos))

            if len(trimestre_uno) == 0:
                print('There were zero reports')
            else:
                suma_de_notas_tres = sum(trimestre_rechazado)
                promedio_tres =suma_de_notas_tres/(len(trimestre_rechazado))

            if len(trimestre_rechazado) + len(trimestre_uno)+ len(trimestre_dos) == 0:
                print('')
            else:
                suma_de_notas_total = suma_de_notas_uno + suma_de_notas_dos + suma_de_notas_tres
                promedio_total =suma_de_notas_total/(len(trimestre_rechazado) + len(trimestre_uno)+ len(trimestre_dos))

            #counters
            print('\n --------TOTAL COUNTERS---------')
            print(f'the total of aspiring students today was of {aspiring_studentcount}')
            print(f'the total amount of aspiring students in trimester one is {len(trimestre_uno)}')
            print(f'the total amount of aspiring students in trimester two is {len(trimestre_dos)}')
            print(f'the total amount of denied students is {len(trimestre_rechazado)} \n')
            #promedios
            print('\n-------PROMEDIOS----------')
            print(f'El promedio de los estudiantes del trimestre uno es igual a {promedio_uno}')
            print(f'El promedio de los estudiantes del trimestre dos es igual a {promedio_dos}')
            print(f'El promedio de los estudiantes del trimestre tres es igual a {promedio_tres}')
            print(f'El promedio de los estudiantes es igual a {promedio_total} \n')

        elif option ==3:
            print('Thank you for coming!')

        else:
            print('Something went wrong. Please enter a valid value.')
            
main()