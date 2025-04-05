# Filtrando productos en oferta

productos = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 300,
    "Auriculares": 80,
    "Impresora": 150
}

# Crea un nuevo diccionario que solo contenga los productos con un precio menor a 100.
# Imprime el resultado.

def productos_en_oferta(listado): 
    return {k: v for k, v in listado.items() if v < 100}

print(productos_en_oferta(productos))
# imprime => 
# {
#     'Mouse': 25,
#     'Teclado': 45,
#     'Auriculares': 80
# }
def products(listado): 
    return {"products": {k: v for k, v in listado.items() if v < 100}}


print(productos_en_oferta(productos))  
# imprime =>
# {
#     'products': {
#         'Mouse': 25,
#         'Teclado': 45,
#         'Auriculares': 80
#     }
# }