import re 

# *:  'Comodin' puede aparecer 0 o mas veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)
['aaa', '', 'a', '']
        #aca 
        #aparece
        #0 veces la 
        #a 
        #por eso 
        #es que te 
        #devuelve 
        #una ''
    
# +: El patron DEBE APARECER AL MENOS UNA o mas veces
text = "dddd aaa ccc bb"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)
# Devuelve todas las coincidencias de 'a' en la string


# ?: una o mas veces
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# {n}: te muestra las apariciones del char si cumple con minimo n veces
#  apenas encuentra n, ya te la devuelve y sigue buscando
# las busca sin importar si hay espacios en el medio, no tiene porque
# solo buscar las que estan unidas
text = "aaaaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)

# podes indicarle un rango:
# si aparece n veces ya te lo devuelve, pero si el proximo es de mas de
# n, analiza si hay por lo menos m y te devuelve m
text = "u uu uuu u"
pattern = "u{2,3}"
matches = re.findall(pattern, text)
print(matches)

# EJERCICIO
# Encuentra las palabras de 4 a 6 letras en el sig texto 
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# EJERCICIO
# Encuentra las palabras de mas de 6 letras
# Si pones solo , sin 'm' entonces es MAS o IGUAL de n veces
words = "ala casa árbosl león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)