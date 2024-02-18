# Tarea 1 Programación 3

## Tarea realizada por:

- Walter Daniel Eliú Gomar González 9490-22-8616 100%
- Andrés Emanuel Chaj Camey 9490-22-9801 100%
- Daniel Alejandro Martinez Ruiz 9490-22-4698 100%

## ¿Cómo usar nuestro programa?

### Iniciar el programa

Para realizar esto simplemente debemos abrir una consola en la ruta donde se encuentre el
archivo, y ejecuar un sólo comando, dependiento de que sistema operativo usemos, este puede variar;

- MacOS y Linux: python3 ./lista_doblemente_enlazada.py
- Windows: py ./lista_doblemente_enlazada.py

A partir de esto, el programa es bastante intuitivo y bastará con ingresar lo que se solicita

### Insertar datos al inicio de la lista

Para ingresar a esta opción, en el menú inicial debemos ingresar el valor de _1_, luego el
programa va a solicitar la informasción del alumno que desea ingresar a la lista.
El programa solicita un nombre, **_sin apellido, sólo el primer nombre_**, seguido de esto, se nos va
a solicitar el apellido, de **_de nuevo, únicamente el primer apellido del estudiante_**. Y para finalizar
se nos pedirá que ingresemos el carné del estudiante, el cual debe estar conformado únicamente por numeros.

### Insertar datos al final de la lista

La funcion de ingresar datos al final (se selecciona con el número _2_) funciona exactamente
igual que la funcion de ingresar datos al comienzo, solicita ingresar los mismos datos, en el
mismo orden, de la misma forma. La única diferencia es que como su nombre lo indica, los datos
que se ingresen serán ingresados al final de la lista.

### Mostrar la lista

Esta función a diferencia del resto, no necesita de ningun parametro, simplemente hay que seleccionarla en el
menú con el número _3_ y se van a imprimir en consola todos los datos que estés almacenados en la lista. en
caso de que no haya ningún dato, el programa se lo hará saber al usuario.

### Eliminar de la lista un valor específico

Esta función se encarga de eliminar un registro de la lista, lo único que necesita como parametro para poder
funcionar es que ingresemos el carné del estudiante. El programa está preparado poder eliminar un registro ya
sea que esté al comienzo de la lista, al final o en cualquier posición de la lista (o si es el último registro).

#### A tomar en cuenta

Si no conoce que carné corresponde a que estudiante, siempre puede recurrir a la funcion de mostrar la lista.

### Salir del programa

Para poder salir del programa, basta con ingresar el número _5_ en el menú principal.
