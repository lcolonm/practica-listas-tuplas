from tuplas_01 import inventario_base
import interfaz

# lvl 2: Manipulación (métodos + slicing)
def agregar_producto(inventario_base):
    lista = list(inventario_base)

    # Envolver todo en una lista contenedora (como tuplas, para mantener la consistencia)
    lista.extend([
        ("Botella de agua", 5.0),
        ("Pechuga de pollo", "Inventario agotado")
        ])
    
    inventario_actualizado = tuple(lista)
    producto, precio = inventario_actualizado[-1]
    
    interfaz.mostrar_dato(producto, precio)
    print(interfaz.SEPARADOR_LARGO)

    return inventario_actualizado, producto, precio


def agregar_por_posicion(inventario_actualizado, indice):

    lista = list(inventario_actualizado)
    lista.insert(indice, ("Aguacate", 4.7))
    inventario_actualizado = tuple(lista)

    nuevo_producto, nuevo_precio = inventario_actualizado[indice]

    print(interfaz.SEPARADOR_LARGO)
    interfaz.mostrar_banner("📝 INVENTARIO ACTUALIZADO 📝")

    for producto, precio in inventario_actualizado:

        if isinstance(precio, (int, float)):
            interfaz.mostrar_dato(producto, f"${precio:.2f}")
        else:
            interfaz.mostrar_dato(producto, precio)

    return inventario_actualizado, nuevo_producto, nuevo_precio


def eliminar_producto(inventario, nombre):
    # 1. Eliminar por nombre
    buscador = inventario.index(nombre)
    
    for eliminar in buscador:
        if eliminar == buscador:
            inventario.remove(buscador)
        else:
            print("No se encontro el producto. Intente de nuevo con otro nombre.")
        






def programa_secundario():

    inventario_actualizado, producto, precio = agregar_producto(inventario_base)

    inventario_actualizado, nuevo_producto, nuevo_precio = agregar_por_posicion(inventario_actualizado, 3)

programa_secundario()
