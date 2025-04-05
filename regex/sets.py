import re

"""
[:] Todo lo que vaya ahi adentro, se pide que coincida con solo esos
Pueden estar o no estarlo, pero NO pueden haber otros simbolos 
que no esten indicados dentro del []
En este ejemplo, se indica que los caracteres validos son: 
 - Alfanumerico, puntos, mas, menos, guion bajo y porcentaje 
Y le decimos a re que mire desde el principio hasta el final, o sea
toda la string
""" 

username = "rubius_69+"
pattern = r"^[\w._%+-]+$"
match = re.search(pattern, username)

print(f"El nombre de usuario {"es" if match else "no es"} valido")

# EJERCICIO
# Buscar todas las vocales del texto
text = "Hola mundo"
pattern = r"[aeiuo]"
matches = re.search(pattern, text)
print(matches.group())

# Se puede usar combinandolo con otro patron para escribir menos
# por ejemplo queres buscar todas palabras que terminan en cion
# IMPORTANTE en este caso tuve que usar el * para caputar todas las letras
# Si no estuviera puesto, me devolveria solo una letra y despues cion
text = "vocacion oracion perdicion"
pattern = r"[a-z]*cion"
matches = re.findall(pattern, text)
print(matches)

# tambien podes encontrar rangos, por ejemplo el patron de solo numeros del 4 al 9
num = "22"
pattern = r"[4-9]"
matches = re.findall(pattern, num)
print(matches)

# caso feliz
num = "41"
pattern = r"[4-9]"
matches = re.findall(pattern, num)
print(matches)

# [^] : podemos fusionarlo con el operador ^ para NEGAR
#  o sea la usuariamos para decir que NO TIENEN que aparecer en mi patron
# EJERCICIO
# Buscar SOLO LAS CONSONANTES del texto
text = "Hola mundo"
pattern = r"[^aeiuo]"
matches = re.findall(pattern, text)
print(matches)
