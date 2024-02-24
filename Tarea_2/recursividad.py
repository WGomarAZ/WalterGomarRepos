import os
import msvcrt
import math


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

def calcular_raiz_cuadrada(n):
    return int(math.sqrt(n))

def raiz_cuadrada_entera(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return calcular_raiz_cuadrada(n)

def raiz():
    os.system("cls")
    print("Raiz cuadrada entera\n")
    valor = int(
        input("Ingrese un numero para obtener su raiz cuadrada entera: "))
    resultado = raiz_cuadrada_entera(valor)

    if resultado == -1:
        os.system("cls")
        print("Los numeros negativos no tienen raiz cuadrada real.")
    elif resultado == 0:
        os.system("cls")
        print(f"La raiz cuadrada de {valor} es: {resultado}")
    else:
        os.system("cls")
        print(f"La raiz cuadrada de {valor} es: {resultado}")

    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()   

conversiones = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def convertir_a_decimal(n):
    if len(n) == 0:
        return 0
    if len(n) == 1:
        return conversiones.get(n[0], 0)  # Utilizamos get() para evitar KeyError
    if conversiones.get(n[0], 0) < conversiones.get(n[1], 0):
        return -conversiones.get(n[0], 0) + convertir_a_decimal(n[1:])
    else:
        return conversiones.get(n[0], 0) + convertir_a_decimal(n[1:])
    

def contar():
    os.system("cls")
    print("Contador de dígitos")
    valor = int(input("Ingrese un numero para poder contar los dígitos que lo conforman "))
    numero = valor
    resultado = contar_digitos(numero)
    if resultado == 0:
        os.system("cls")
        print ("Ingrese un número diferente de 0")
    else: 
        os.system("cls")
        print(f"{numero} tiene {resultado} dígitos")
    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()

def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n/10)


def decimal():
    os.system("cls")
    print("Conversion a decimal desde romano\n")
    valor = input(
        "Ingrese un numero romano para convertirlo a sistema decimal: ")
    romano_mayus = valor.upper()
    resultado = convertir_a_decimal(romano_mayus)

    if resultado == 0:
        os.system("cls")
        print("Debe ingresar un numero para poder convertir")
    else:
        os.system("cls")
        print(f"{romano_mayus} en sistema decimal es: {resultado}")

    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()


def enteros():
    os.system("cls")
    print("Suma de numeros enteros")
    valor = int(input("Ingrese un numero entero para realizar la sumatoria de sus predecesores hasta el numero ingresado "))
    numero = valor
    resultado = suma_numeros_enteros(numero)
    if resultado == 0:
        os.system("cls")
        print ("Ingrese un número diferente de 0")
    else: 
        os.system("cls")
        print(f"La suma de los numeros hasta {numero} es {resultado}")
    print("\nPresiona cualquier tecla para continuar...")
    msvcrt.getch()

def suma_numeros_enteros(n):
    if n == 0:
        return 0
    else:
        return n + suma_numeros_enteros(n-1)

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
