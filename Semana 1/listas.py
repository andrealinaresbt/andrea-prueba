estudiantes = ['Andres', 'Maria' , "Isabel"]
for i in range(0, len(estudiantes)):
    print(estudiantes[i])

print("""
""")
for u in range(len(estudiantes)-1, -1, -1):
    print(estudiantes[u])

print("""
""")

for estudiante in estudiantes:
    if estudiante == "Maria":
        print('No me gusta tu cabello Maria')
        pass
    print (f'Bienvenido a la clase {estudiante}')

#append es para agregar a la lista
#borras con pop por indice
