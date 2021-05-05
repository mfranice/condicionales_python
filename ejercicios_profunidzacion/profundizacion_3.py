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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = float(input('Ingrese la primera temperatura en grados centígrados:\n'))
temperatura_2 = float(input('Ingrese la segunda temperatura en grados centígrados:\n'))
temperatura_3 = float(input('Ingrese la tercera temperatura en grados centígrados:\n'))

if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
    print('La máxima temperatura ingresada es la temperatura 1:', temperatura_1)
elif temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
    print('La máxima temperatura ingresada es la temperatura 2:', temperatura_2)
else:
    print('La máxima temperatura ingresada es la temperatura 3:', temperatura_3)


if temperatura_1 < temperatura_2 and temperatura_1 < temperatura_3:
    print('La mínima temperatura ingresada es la temperatura 1:', temperatura_1) 
elif temperatura_2 < temperatura_1 and temperatura_2 < temperatura_3:
    print('La mínima temperatura ingresada es la temperatura 1:', temperatura_2)
else:
    print('La mínima temperatura ingresada es la temperatura 1:', temperatura_3)


temp_promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3
print('El promedio de las temperaturas ingresadas es:', temp_promedio)
