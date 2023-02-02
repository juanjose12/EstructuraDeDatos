
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


    diflist = []
    for i in listaA:
        if i not in listaB:
            diflist.append(i)


#Pregunta 4
"""Escriba la definición de la operación mostrarPrimos que reciba como parámetro
un valor N y muestre los números primos desde 1 hasta N. En adición a esto, esta operación
debe también mostrar entre esos números primos cuáles tienen la particularidad de que la suma
de sus dígitos también da un número primo. Los resultados deben ser imprimidos siguiendo el
formato que se indica a continuación."""


def mostrarPrimos(n):

    numero = 0
    while numero <= n:
        cont = 1
        x = 0
        while cont <= numero:
            if numero % cont == 0:
                x += 1
            cont += 1
        if x == 2:
            print("-->", numero, ",")

        numero += 1


print(mostrarPrimos(100))
