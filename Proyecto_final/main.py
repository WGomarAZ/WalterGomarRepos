import os
import integrantes


def case1():
    os.system("cls")
    print("CASO UNO")
    input("\nPRESIONE 'ENTER' PARA CONTINUAR...")


def case2():
    os.system("cls")
    print("CASO DOS")
    input("\nPRESIONE 'ENTER' PARA CONTINUAR...")


def case3():
    integrantes.integrantes()


opciones = {1: case1, 2: case2, 3: case3}

while True:
    os.system("cls")
    print("SELECCIONE UNA OPCION\n")
    print("1. JUGAR")
    print("2. HISTORIAL DE Y NÚMERO DE APRENDIZAJES NECESARIOS")
    print("3. VER INTEGRANTES DEL GRUPO")
    print("4. SALIR\n")

    opcion = input("INGRESE EL VALOR CORRESPONDIENTE A SU SELECCION: ")

    try:
        opcion = int(opcion)

        if opcion in opciones:
            opciones[opcion]()
        elif opcion == 4:
            os.system("cls")
            print("SALIENDO DEL PROGRAMA...")
            input("PRESIONE 'ENTER' PARA CONTINUAR...")
            break
        else:
            os.system("cls")
            print(f"OPCION '{opcion}', INEXISTENTE\n")
            input("PRESIONE 'ENTER' PARA CONTINUAR...")

    except ValueError as err:
        os.system("cls")
        print(f"DEBE INGRESAR UN VALOR NUMERICO\n{err}")
        input("\nPRESIONE 'ENTER' PARA CONTINUAR...")
