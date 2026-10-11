# Librería de diseño lindo para la consola

# --- SIMBOLOS Y ESTILOS ---
SEPARADOR_CORTO = f"✨ {'─' * 25} ✨"
SEPARADOR_LARGO = f"✨ {'─' * 35} ✨"

# --- FUNCIONES DECORADORAS ---

def mostrar_exito(mensaje):
    print(f"\n{SEPARADOR_LARGO}")
    print(f"  ✔ {mensaje}")
    print(f"{SEPARADOR_LARGO}\n")


def mostrar_banner(titulo="📝 INVENTARIO DE PRODUCTOS 📝"):
    # 1. Calculamos el ancho basado en la longitud del título, 
    # pero aseguramos que sea al menos de 35 (o el tamaño del texto + un margen de respiro)
    ancho = max(35, len(titulo) + 4)
    
    print(f"╭{'─' * ancho}╮")
    print(f"│{titulo.center(ancho)}│")
    print(f"╰{'─' * ancho}╯")
    print()


def mostrar_dato(etiqueta: str | int | float | None = "", valor: str | int | float | None = ""):
    # 1. Normalizar si vienen como None
    if etiqueta is None:
        etiqueta = ""
    if valor is None:
        valor = ""

    # 2. Convertir a string de forma segura
    etiqueta_str = str(etiqueta)
    valor_str = str(valor)

    # 3. Si no hay valor, muestra solo la etiqueta
    if not valor_str:
        print(f"  ► {etiqueta_str}")
    else:
        print(f"  ► {etiqueta_str:<15}: {valor_str:>10}")


# --- MOSTRAR INVENTARIO GENÉRICO ---
def mostrar_inventario(inventario, titulo="📝 INVENTARIO DE PRODUCTOS 📝"):
    print(f"\n{SEPARADOR_LARGO}")
    mostrar_banner(titulo)

    for producto, precio in inventario:
        if isinstance(precio, (int, float)):
            mostrar_dato(producto, f"${precio:.2f}")
        else:
            mostrar_dato(producto, precio)
            
    print(f"{SEPARADOR_LARGO}\n")