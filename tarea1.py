
# Pregunta 1
"""Escriba la definición de la operación verificarDiagonales que dada una matriz
cuadrada, revise si en cada fila, el elemento de la diagonal principal es el mismo elemento de la
diagonal secundaria. En caso de que todos los elementos coincidan se debe retornar True, de
lo contrario False. A partir de lo anterior, si se tiene una matriz mat como sigue"""


def verificarDiagonales(mat):

    ndiag1 = []
    ndiag2 = []
    # Encontrar Diagonal 1
    for i in range(len(mat)):
        diag1 = mat[i][i]
        ndiag1.append(diag1)
        # Encontrar Diagonal 2
        for j in range(len(mat)):
            diag2 = mat[j][j-1]
            ndiag2.append(diag2)
    # Comparar diagonales
    for a in range(len(ndiag1)):
        if (ndiag1[a] != ndiag2[a]):
            return False
        else:
            return True


# Pregunta 2
"""Escriba la definición en Python de la operación esCapicua que dada una lista de
números enteros revisar si la lista es capicúa, es decir, que los números de izquierda a derecha,
se lee igual de que los número de derecha a izquierda. De esta manera, una invocación como la
siguiente:"""


def esCapicua(list):

    rlist = list[::-1]
    for i in range(len(list)):
        if list[i] != rlist[i]:
            return False
        else:
            return True


# Pregunta 3
# Parte A
"""Escriba la definición de la operación diferenciaListas que dadas 2 listas de números
enteros construya una lista cuyo contenido corresponde a la diferencia entre ambas listas,
i. e., los elementos que quedan en la primera lista al no tener en cuenta los elementos que
tiene en común con la segunda lista. A partir de lo anterior, si se consideran las siguientes
dos listas"""


def diferenciarListas(listaA, listaB):

# Imprimir los numeros que no comparten las dos listas
# Si lo que se encuentra en B esta en A quitar el ese numero indexado
    temp = []
    for i in range(len(listaB)):
        if (listaB[i] in listaA):
            temp.append(listaA[i])
    return temp

# Parte B
"""Escriba la definición de una operación de lectura e impresión de datos en la que primera
se lea un número correspondiente a la cantidad de ejecuciones a realizar. Posteriormente,
para cada ejecución se deben leer dos líneas. En cada línea debe aparecer primero un valor
n correspondiente a la cantidad de datos en cada lista y luego n valores correspondientes a
los datos que deben contener las listas. La primera línea tiene los datos de la primera lista
que se debe pasar a la función diferenciaListas y la segunda línea tiene los datos
de la segunda lista. Para cada ejecución se debe imprimir los valores en la lista resultante
separados con comas."""

# Pregunta 4
"""Escriba la definición de la operación mostrarPrimos que reciba como parámetro
un valor N y muestre los números primos desde 1 hasta N. En adición a esto, esta operación
debe también mostrar entre esos números primos cuáles tienen la particularidad de que la suma
de sus dígitos también da un número primo. Los resultados deben ser imprimidos siguiendo el
formato que se indica a continuación."""


def mostrarPrimos(N):
    def sum_of_digits(n):
        return sum(int(d) for d in str(n))

    def isPrime(n):
        if (n < 1):
            return False
        else:
            for i in range(2, n):
                if (n % i == 0):
                    return False  # No es primo
            return True  # Es primo 

    n_primos = []
    for i in range(2, N+1):
        if isPrime(i):
            n_primos.append(i)
    d_primos = []
    for i in n_primos:
        if isPrime(sum_of_digits(i)):
            d_primos.append(i)
    for i in range(len(n_primos)):
        print("--> ", n_primos[i], end = ", \n")
    print("Números entre 1 y 100 con suma de dígitos con valor primo:")
    for i in range(len(d_primos)):
        print(d_primos[i], end =", ")


# Pregunta 5
"""Escriba la definición de la operación sumarValoresMatriz que reciba una matriz dispersa
(diccionario) mat y una lista de parejas par correspondientes a posiciones en la matriz y debe
retornar la suma de los valores en la matriz en dichas posiciones."""


def sumarValoresMat(matriz, nPares):
    sum = 0
    for i, j in nPares:
        sum += matriz[i][j]
    return sum
