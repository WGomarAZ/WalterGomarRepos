import os
import msvcrt


class Node:
    def __init__(self, numero):
        self.numero = numero
        self.izquierda = None
        self.derecha = None


class Arbol_Busqueda_Binario:
    def __init__(self):
        self.root = None

    def insertar_numero(self, numero, nodo):
        if nodo is None:
            return Node(numero)

        if numero < nodo.numero:
            nodo.izquierda = self.insertar_numero(numero, nodo.izquierda)

        if numero > nodo.numero:
            nodo.derecha = self.insertar_numero(numero, nodo.derecha)

        return nodo

    def buscar_numero(self, numero, nodo):
        if nodo is None:
            return None

        if nodo.numero == numero:
            return nodo

        if numero < nodo.numero:
            return self.buscar_numero(numero, nodo.izquierda)

        if numero > nodo.numero:
            return self.buscar_numero(numero, nodo.derecha)

    def encontar_sucesor(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    def eliminar_numero(self, numero, nodo):
        if nodo is None:
            return nodo

        if nodo.numero == numero and nodo.izquierda is None and nodo.derecha is None:
            return None

        if nodo.numero == numero:
            if nodo.izquierda is None:
                return nodo.derecha
            if nodo.derecha is None:
                return nodo.izquierda

            sucesor = self.encontar_sucesor(nodo.derecha)
            nodo.numero = sucesor.numero
            nodo.derecha = self.eliminar_numero(sucesor.numero, nodo.derecha)

        if numero < nodo.numero:
            nodo.izquierda = self.eliminar_numero(numero, nodo.izquierda)

        if numero > nodo.numero:
            nodo.derecha = self.eliminar_numero(numero, nodo.derecha)

        return nodo


# LEER ARCHIVOS
numeros = []


def leer_archivo(ruta):
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea_numero = int(linea)
                numeros.append(linea_numero)
    except FileNotFoundError as err:
        print(f"\nError! El archivo '{ruta}' no se encontró.\n{err}")
    except Exception as err:
        print(f"\nError! Algo salió mal.\n")


# CREAMOS LA INSTANCIA PARA ACCEDER A LAS FUNCIONES Y VALORES
arbol = Arbol_Busqueda_Binario()


# FUNCION PARA INSERTAR DATOS MANUALMENTE
def insertar():
    os.system("cls")
    print("A continuación deberá ingresar los número que desee insertar en el arbol.")
    print("Ingrese \"fin\" para detener la lectura de datos.\n")

    while True:
        valor = input("Ingrese el número que desea insertar en el arbol: ")

        if not valor.isdigit():
            valor = valor.lower()
            if valor == "fin":
                print("\nNumeros ingresados correctamente.")
                print("Presione cualquier tecla para continuar...")
                msvcrt.getch()
                break
            else:
                os.system("cls")
                print(
                    "Debe ingresar un número o la palabra \"fin\" para detener la lectura de datos.")
                print("Presione cualquier tecla para continuar...")
                msvcrt.getch()
        else:
            valor = int(valor)
            arbol.root = arbol.insertar_numero(valor, arbol.root)


# FUNCION PARA BUSCAR DATOS
def buscar():
    os.system("cls")
    valor = int(input("Ingrse el número que desea búscar en el arbol: "))
    resultado = arbol.buscar_numero(valor, arbol.root)

    if resultado is None:
        print("\nEl número que busca no se encuentra dentro del arbol.")
    else:
        print(f"\nEl número {resultado.numero} se encuentra dentro del arbol")

    print("Presione cualquier tecla para continuara...")
    msvcrt.getch()


# FUCNION PARA ELIMINAR DATOS
def eliminar():
    os.system("cls")
    valor = input("Ingrese el número que desea eliminar del arbol: ")
    if not valor.isdigit():
        print("\nEl dato a ingresar debe ser un número.")
        print("Presione cualquier tecla pra continuar...")
        msvcrt.getch()
    else:
        valor = int(valor)
        arbol.root = arbol.eliminar_numero(valor, arbol.root)

        if arbol.root is not None:
            print("\nEl número se eliminó correctamente.")
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()


# FUNCION PARA CARGAR DATOS DESDE UN ARCHIVO
def cargar():
    os.system("cls")
    # FORMATO PARA LA RUTA (SE DEBE HACER MANUAL) "D:\\Uni\\Programación III\\Grupo\\WalterGomarRepos\\Tarea_3\\datos.txt"
    ruta_archivo = input(
        "Ingrese la ruta de su archivo para cargar los datos: ")
    leer_archivo(ruta_archivo)

    for numero in numeros:
        arbol.root = arbol.insertar_numero(numero, arbol.root)
    print("\nDatos del archivo cargados")
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()


# FUNCION PARA SALIR DEL PROGRAMA
def salir():
    os.system("cls")
    print("Saliendo del programa, presione cualquier tecla para continuar...\n")
    msvcrt.getch()
    exit()


# SE DEFINE LA FUNCION PRINCIPAL QUE EJECUTA EL MENÚ Y LA LOGÍSTICA PARA LA PRESENTACIÓN DEL PROGRAMA
def menu():
    opciones = {
        1: insertar,
        2: buscar,
        3: eliminar,
        4: cargar,
        5: salir
    }

    # CICLO PARA IMPRIMIR EL MENÚ
    while True:
        os.system("cls")
        print("Bienvenido a nuestro programa de interacciones con un arbol binario.")
        print("A continuación, ingrese el número correspondiente a la acción que desea realizar\n")
        print("1. Insertar datos al arbol")
        print("2. Buscar un dato del arbol")
        print("3. Eliminar un dato del arbol")
        print("4. Cargar datos desde un archivo .txt")
        print("5. Salir\n")
        opcion = input("Su opcion: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion in opciones:
                opciones[opcion]()
            else:
                print("Opcion no encontrada dentro de las funciones")
        else:
            print("Error, debe ingresar un número")


# SE EJECUTA EL MENU
menu()
