import interfaz

"""
Programa que gestiona un inventario de una tienda. 
Cada producto es una tupla, el inventario es una lista de esas tuplas.
"""

# lvl 1: Fundamentos
def crear_inventario():
    inventario = [
        ("manzana", 1.5),
        ("pan", 2.0),
        ("leche", 3.5),
        ("huevos", 0.5),
        ("arroz", 2.5),
    ]
    return inventario


def mostrar_inventario(inventario):
    print(interfaz.SEPARADOR_LARGO)
    interfaz.mostrar_banner("📝 INVENTARIO DE PRODUCTOS 📝")

    for producto, precio in inventario:
        interfaz.mostrar_dato(producto, f"${precio:.2f}")


def contar_productos(inventario):
    cantidad = len(inventario)
    
    # Desempaquetamos para tener los nombres limpios
    nombre_primero, precio_primero = inventario[0]
    nombre_ultimo, precio_ultimo = inventario[-1]

    print(interfaz.SEPARADOR_LARGO)
    interfaz.mostrar_banner("📊 RESUMEN DE INVENTARIO 📊")
    
    # Pasamos primero la ETIQUETA (texto) y luego el VALOR (dato)
    interfaz.mostrar_dato("Total ítems", cantidad)
    interfaz.mostrar_dato("Primer producto", nombre_primero)
    interfaz.mostrar_dato("Último producto", nombre_ultimo)


def producto_en_posicion(inventario, indice):
    producto, precio = inventario[indice]

    print(interfaz.SEPARADOR_CORTO)
    interfaz.mostrar_dato(f"Posición {indice}", f"{producto} (${precio:.2f})")

    return producto, precio


def programa_principal():
    inventario = crear_inventario()

    mostrar_inventario(inventario)
    contar_productos(inventario)
    
    producto, precio = producto_en_posicion(inventario, 2)


# --- EJECUCIÓN DEL PROGRAMA ---
programa_principal()