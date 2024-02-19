import os
import msvcrt


def convertir_a_binario(n):
    if (n <= 0):
        return ""
    else:
        return convertir_a_binario(n//2)+str(n % 2)


def binario():
    os.system("cls")
    print("Conversion a binario\n")
    numero_decimal = int(input("Ingrese un número para convertir a binario: "))
    numero_binario = convertir_a_binario(numero_decimal)

    if (numero_binario == ""):
        os.system("cls")
        print(f"{numero_decimal} en el sistema binario es igual a: 0")
    else:
        os.system("cls")
        print(str(numero_decimal) +
              " en el sistema binario es igual a: "+numero_binario)

    print("\nPresione cualquier tecla para continuar...")
    msvcrt.getch()


def contar():
    os.system("cls")
    print("Contar digitos")
    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()


def raiz():
    os.system("cls")
    print("Raiz cuadrada")
    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()


def decimal():
    os.system("cls")
    print("Conversion a decimal")
    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()


def enteros():
    os.system("cls")
    print("Suma de numeros enteros")
    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()


def salir():
    os.system("cls")
    print("Saliendo del programa")
    print("\nPresione cualquier tecla para continuar...")
    msvcrt.getch()
    exit()


def defecto():
    os.system("cls")
    print("Opcion invalida, debe ingresar un numero entre el 1 y el 5 incluyendo ambos extremos.")
    print("\nPresione cualquier tecla para continuar...")
    msvcrt.getch()


while (True):
    os.system("cls")
    print("TAREA NO. 02\n")
    print("Seleccione una opcion")
    print("1. Convertir a binario")
    print("2. Contar digitos")
    print("3. Raiz cuadrada entera")
    print("4. Convertir a decimal desde romano")
    print("5. Suma de numeros enteros")
    print("0. Salir")

    try:
        opcion = int(input("\nSeleccione una opcion: "))

        if (opcion == 1):
            binario()
        elif (opcion == 2):
            contar()
        elif (opcion == 3):
            raiz()
        elif (opcion == 4):
            decimal()
        elif (opcion == 5):
            enteros()
        elif (opcion == 0):
            salir()
        else:
            defecto()

    except (ValueError):
        os.system("cls")
        print("Opcion invalida, no se admite texto.")
        print("\nPresione cualquier tecla para continuar...")
        msvcrt.getch()
