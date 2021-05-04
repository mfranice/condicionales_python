# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('La primera palabra ingresada ({}) es mayor (alfabeticamente) que la segunda ({})'.format(texto_1,texto_2))
elif texto_1 < texto_2:
    print('La segunda palabra ingresada ({}) es mayor (alfabeticamente) que la primera ({})'.format(texto_2,texto_1)) 
else:
    print('Ambas palabras ingresadas ({}) son iguales'.format(texto_1,texto_2))

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print('La primera palabra ingresada ({}) es más larga que la segunda ({})'.format(texto_1,texto_2))
elif len(texto_1) < len(texto_2):
    print('La segunda palabra ingresada ({}) es más larga que la primera ({})'.format(texto_2,texto_1)) 
else:
    print('Ambas palabras ingresadas ({} y {}) tienen la misma cantidad de letras'.format(texto_1,texto_2))

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1 [0] > texto_2[0]:
    print('La primera letra de la primera palabra ingresada ({}) es mayor que la de la segunda ({})'.format(texto_1,texto_2))
elif texto_1 [0] < texto_2 [0]:
    print('La primera letra de la segunda palabra ingresada ({}) es mayor que la de la primera ({})'.format(texto_2,texto_1)) 
else:
    print('Las primeras letras de ambas palabras ingresadas ({} y {}) son iguales'.format(texto_1,texto_2))


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if texto_1 == copia_texto_1:
    print('La variable copia_texto_1 ({}) es igual a la variable texto_1 ({})'.format(copia_texto_1,texto_1))
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if texto_1 != copia_texto_1:
    print('La variable copia_texto_1 ({}) es igual a la variable texto_1 ({})'.format(copia_texto_1,texto_1))