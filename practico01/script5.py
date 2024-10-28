# Crear un diccionario con tres pares de clave:valor de tipos diferentes
mi_diccionario = {
    "nombre": "Juan",          # String
    2: 100,                    # Integer como clave
    (1, 2): [10, 20, 30]       # Tupla como clave y lista como valor
}

# Imprimir el diccionario inicial
print("Diccionario inicial:", mi_diccionario)

# Imprimir el valor de la primera clave
print("Valor de la primera clave 'nombre':", mi_diccionario["nombre"])

# Añadir un nuevo par clave:valor al diccionario
mi_diccionario["edad"] = 25
print("Diccionario después de añadir un nuevo par clave:", mi_diccionario)

# Cambiar el valor de la segunda clave existente
mi_diccionario[2] = 2000


# Imprimir el contenido completo del diccionario
print("Contenido final de mi_diccionario:", mi_diccionario)
