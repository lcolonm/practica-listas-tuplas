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

    interfaz.mostrar_inventario(inventario_actualizado, "📝 INVENTARIO DE PRODUCTOS ACTUALIZADO 📝")

    return inventario_actualizado, nuevo_producto, nuevo_precio


def eliminar_producto(inventario, nombre):
    lista = list(inventario) # Por seguridad pasamos a lista.
    
    for producto, costo in lista:
        if producto == nombre:
            # El método .remove busca y borra el elemento exacto tal como viene 
            # por ello le pasamos la tupla completa.
            lista.remove((producto, costo)) 
            interfaz.mostrar_exito(f"'{nombre}' eliminado con éxito.")
            break  # Rompe el bucle porque ya lo encontró.
    else:
        # Este else pertenece al FOR, no al IF. 
        # Solo se ejecuta si el bucle terminó todas sus vueltas y nunca tocó el break.
        print(f"⚠️ No se encontró el producto '{nombre}'.")

    inventario_actualizado = tuple(lista)

    interfaz.mostrar_inventario(inventario_actualizado, "📝 INVENTARIO DE PRODUCTOS ACTUALIZADO 📝")

    return inventario_actualizado
           
def programa_secundario():

    inventario_actualizado, producto, precio = agregar_producto(inventario_base)

    inventario_actualizado, nuevo_producto, nuevo_precio = agregar_por_posicion(inventario_actualizado, 3)

    inventario_actualizado = eliminar_producto(inventario_actualizado, "Pechuga de pollo")

programa_secundario()
