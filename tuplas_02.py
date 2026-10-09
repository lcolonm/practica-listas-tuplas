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
    return inventario_actualizado, producto, precio

def programa_secundario():
    # ------- Primera parte + decoración ---------
    inventario_actualizado, producto, precio = agregar_producto(inventario_base)
    print()
    interfaz.mostrar_dato(producto, precio)
    print(interfaz.SEPARADOR_LARGO)

    # ------- Segunda parte en construcción.... ---------

programa_secundario()
