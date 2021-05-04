# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# Verifique cual de los dos textos es mayor alfabéticamente
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('El texto_1 ({}) es mayor alfabéticamente que el texto_2 ({})'.format(texto_1, texto_2))
else:
    print('El texto_1 ({}) es menor alfabéticamente que el texto_2 ({})'.format(texto_1, texto_2))    

# Transforma esas variables tipo texto y almacénalas
# en nuevas variables númericas (int)
# Repita el proceso, ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

try:
    numero_1 = int(texto_1)
    numero_2 = int(texto_2)
except:
    print('No se puede leer uno de los textos como un número entero')

if numero_1 > numero_2:
    print('El entero correspondiente al texto_1 ({}) es mayor que el entero correspondiente al texto_2 ({})'.format(numero_1, numero_2))
else:
    print('El entero correspondiente al texto_1 ({}) es menor que el entero correspondiente al texto_2 ({})'.format(numero_1, numero_2))

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
