''' Porcentaje de materia = (C * 100)/ NC = P%
NC = numero de creditos
C = Creditos
Acumulado = (p% /100)* grade'''


def calcular_acumulado_semestre():
    try:
        num_materias = int(input("Ingrese el número de materias a registrar: "))
        num_creditos_semestre = int(input("Ingrese el número de créditos registrados en el semestre: "))
        final_percentage = []

        for _ in range(num_materias):
            nombre_materia = input("Ingrese el nombre de la materia: ")
            creditos_materia = int(input(f"Cuantos créditos tiene {nombre_materia}: "))
            nota_obtenida = float(input(f"Cual fue su nota obtenida en {nombre_materia}: "))
            porcentaje = (creditos_materia * 100) / num_creditos_semestre
            acumulado = (porcentaje / 100) * nota_obtenida
            final_percentage.append(acumulado)

        calculo = sum(final_percentage)
        print(f" \n Su acumulado final es: {calculo:.2f} \n")

    except ValueError:
        print("Ha ocurrido un error. Por favor, asegúrese de ingresar números válidos.")




def menu():
    flag = True
    print('''! Hola Bienvenido a la calculadora de semestre ! \n 
          A continuacion selecciona una de las opciones : \n''')
    while flag == True:
        
        seleccion = int(input('''\n 1. Calcular acumulado de una materia \n
                                 \n 2. Calcular acumulado semestre \n
                                 \n 3. Salir  \n '''))
        if seleccion == 1:  
                #calcular_acumulado_materia()
                print("no esta definido")
        elif seleccion == 2:
            calcular_acumulado_semestre()
        elif seleccion == 3:
          print(" ! ha salido con exito del sistema  :)  ! ")
          flag = False

        else:
            print("! Algo anda mal, vuelve a intentarlo  :c !")
            
menu()
    
