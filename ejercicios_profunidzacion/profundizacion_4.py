# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra)

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra_1 = str(input('Ingrese la primera palabra:\n'))
palabra_2 = str(input('Ingrese la segunda palabra:\n'))
palabra_3 = str(input('Ingrese la tercera palabra:\n'))

print('Ingrese 1 si desea ordenar las palabras de mayor a menor por orden alfabético')
print('Ingrese 2 si desea ordenar las palabras de mayor a menor por cantidad de letras')
opcion = int(input())

#_______________OPCION 1_______________________________
#Busca cual es la mayor palabra por orden alfabético:
if palabra_1 > palabra_2 and palabra_1 > palabra_3:
    alfabetico_1 =  palabra_1
elif palabra_2 > palabra_1 and palabra_2 > palabra_3:
    alfabetico_1 = palabra_2
else:
    alfabetico_1 = palabra_3

#Busca cual es la menor palabra por orden alfabético:
if palabra_1 < palabra_2 and palabra_1 < palabra_3:
    alfabetico_3 = palabra_1
elif palabra_2 < palabra_1 and palabra_2 < palabra_3:
    alfabetico_3 = palabra_2
else:
    alfabetico_3 = palabra_3

#La palabra del medio es la que no es la mayor ni la menor:
if alfabetico_1 != palabra_1 and alfabetico_3 != palabra_1:
    alfabetico_2 = palabra_1
elif alfabetico_1 != palabra_2 and alfabetico_3 != palabra_2:
    alfabetico_2 = palabra_2
else:
    alfabetico_2 = palabra_3

#_______________OPCION 2_______________________________

#Busca cual es la palabra más larga:
if len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3):
    palabra_larga_1 = palabra_1
elif len(palabra_2) > len(palabra_1) and len(palabra_2) > len(palabra_3):
    palabra_larga_1 = palabra_2
else:
    palabra_larga_1 = palabra_3

#Busca cual es la palabra más corta:
if len(palabra_1) < len(palabra_2) and len(palabra_1) < len(palabra_3):
    palabra_larga_3 =  palabra_1
elif len(palabra_2) < len(palabra_1) and len(palabra_2) < len(palabra_3):
    palabra_larga_3 = palabra_2
else:
    palabra_larga_3 = palabra_3

#La palabra del medio es la que no es la más larga ni la más corta:
if palabra_larga_1 != palabra_1 and palabra_larga_3 != palabra_1:
    palabra_larga_2 = palabra_1
elif palabra_larga_1 != palabra_2 and palabra_larga_3 != palabra_2:
    palabra_larga_2 = palabra_2
else:
    palabra_larga_2 = palabra_3

#_______________IMPRESIÓN EN PANTALLA_______________________

if opcion == 1:
    print(alfabetico_1,'\t', alfabetico_2,'\t', alfabetico_3,'\t')

elif opcion == 2:
    print(palabra_larga_1,'\t', palabra_larga_2,'\t', palabra_larga_3,'\t')
else:
    print('Ingreso por teclado incorrecto.')