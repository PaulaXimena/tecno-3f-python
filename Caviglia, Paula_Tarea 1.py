#Practica 1
#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.
conjunto1= {1, 2, 3, 4, 5}
conjunto2= {4, 5, 6, 7, 8}

conjunto_union= conjunto1|conjunto2

print(conjunto_union)

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B
conjunto1= {1, 2, 3, 4, 5}
conjunto2= {4, 5, 6, 7, 8}

conjunto_interseccion= conjunto1&conjunto2

print(conjunto_interseccion)

#3)Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
conjunto1= {1, 2, 3, 4, 5}
conjunto2= {4, 5, 6, 7, 8}

conjunto_diferencia= conjunto1.symmetric_difference(conjunto2)

print(conjunto_diferencia)

#4)Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.
conjuntoA = {'Rojo', 'Blanco', 'Azul', 'Amarillo','Verde', 'Naranja','Gris'}

conjuntoB = {'Gris','Naranja'}

print(conjuntoB.issubset(conjuntoA))

#5)Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto.

A = {1, 2, 3, 4, 5}


print(len(A))