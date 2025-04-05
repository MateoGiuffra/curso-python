import re 
"""
FUNCIONES CLAVES:

1. findall(pattern, string)  
   - Retorna una lista con todas las coincidencias del patrón en la cadena.  
   - Si hay grupos de captura, devuelve una lista de tuplas con los valores capturados.  

2. search(pattern, string)  
   - Retorna un objeto 'match' con la primera coincidencia encontrada.  
   - Métodos útiles del objeto 'match':  
       - group(): Devuelve la coincidencia completa o la lista de coincidencias.  
       - start(): Índice donde comienza la coincidencia.  
       - end(): Índice donde termina la coincidencia.  

3. match(pattern, string)  
   - Similar a search, pero solo busca coincidencias al inicio de la cadena.  

4. fullmatch(pattern, string)  
   - Retorna un objeto 'match' si toda la cadena coincide con el patrón.  

5. split(pattern, string)  
   - Divide la cadena usando el patrón como separador y devuelve una lista.  

6. sub(pattern, replacement, string)  
   - Reemplaza todas las coincidencias del patrón por la cadena de reemplazo.  
   - Se puede usar un número como argumento extra para limitar la cantidad de reemplazos.  


MODIFICADORES COMUNES:
- re.IGNORECASE (o re.I) => Ignora mayúsculas y minúsculas.  
- re.MULTILINE (o re.M) => Hace que `^` y `$` coincidan con cada línea, no solo con el inicio y fin del texto.  
- re.DOTALL (o re.S) => Hace que `.` coincida con saltos de línea.  
"""


# Encontrar todas las palabras que cumplan con el patron EXACTO. 
text = "python es genial. Python es un lenguaje de programación. PYTHON es versátil."
pattern = r"python"
result = re.findall(pattern, text)
print(result)# => muestra [python]

# Encontrar todas las palabras que cumplan con el patron ignorando mayus/minusculas. 
text = "python es genial. Python es un lenguaje de programación. PYTHON es versátil."
pattern = r"python"
result = re.findall(pattern, text, re.IGNORECASE)
print(result) # => muestra [python, Python, PYTHON]


"""
El patrón r"\w+" coincide con uno o más caracteres alfanuméricos (letras, números y guion bajo). 
En el texto "rubius69" todos los caracteres son alfanuméricos, 
por lo que findall() devuelve la cadena completa como una coincidencia.
LO HACE CON caracteres alfanuméricos JUNTOS, no con caracteres individuales
Si en el medio de la string, hay un valor NO Alfanumerico, entonces ahi si se separa la coincidencia
"""

text = "@elrubius_69"
pattern = r"\w"
result = re.findall(pattern, text)
print(result) # => ['e', 'l', 'r', 'u', 'b', 'i', 'u', 's', '_', '6', '9']

# Obtener cualquier caracter alfanumerico (solo las que son un char)
text = "Hola Pepe como esta y ?"
result = re.findall(r"\b\w\b", text)
print(result) # => muestra  'a'

# Obtener TODAS las palabras de una cadena de textotext = "Hola a Pepe como esta?"
result = re.findall(r"\b\w+\b", text)
print(result) # => muestra '['Hola', 'a', 'Pepe', 'como', 'esta']'  
# Excluye signos especiales como ? ¿ ¡!

def reemplazar_alternado(match): # Alterna entre "NOMBRE" y "EDAD" para cada coincidencia
    reemplazar_alternado.contador = getattr(reemplazar_alternado, "contador", 0) + 1
    return "NOMBRE" if reemplazar_alternado.contador % 2 == 1 else "EDAD"

texto = "Hola, mi nombre es Juan y tengo 30 años."
resultado = re.sub(r"\b\w+\b", reemplazar_alternado, texto, flags=re.IGNORECASE)
print(resultado)


text = "Mi numero de telefono es +54 123443223"
pattern = r"\+54 \d{9}"
found = re.search(pattern, text)
if found: 
    print(f"Encontre el numero de telefono {found.group()}")
    
#  \s para encontrar cualquier espacio en blanco (espaciom tabulacion, salto en linea)
text = "Hola mundo\n¿Como estas?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^:  Coincide con el principio de una cadena 
# Validar nombre de usuario
username = "@pepe"
pattern = r"^\w"
valid = re.search(pattern, username)
print(f"El nombre de usuario {"ES" if valid else "NO es"} valido") 
    
# : Coincide con el final de una cadenausername = "@pepe"
# Validar que un mail sea de gmail
mail = "matute@gmail.com" 
pattern = r"@gmail.com$"
valid = re.search(pattern, mail)
print(f"El mail {"ES" if valid else "NO es"} de GMAIL") 


# Tenemos una lista de archivos, necesitamos saber los nombres 
# de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b\w+\.txt\b"
matches = re.findall(pattern, files)
print(matches)  
