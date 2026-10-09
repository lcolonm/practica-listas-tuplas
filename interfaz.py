# Librería de diseño lindo para la consola

# --- SIMBOLOS Y ESTILOS ---
SEPARADOR_CORTO = f"\n✨ {'─' * 25} ✨\n"
SEPARADOR_LARGO = f"\n✨ {'─' * 35} ✨\n"

# --- FUNCIONES DECORADORAS ---
def mostrar_banner(titulo):
    ancho = 35
    print(f"╭{'─' * ancho}╮")
    print(f"│{titulo.center(ancho)}│")
    print(f"╰{'─' * ancho}╯")
    print()

def mostrar_exito(mensaje):
    print(SEPARADOR_LARGO)
    print(f"  ✔ {mensaje}\n")
    print(SEPARADOR_LARGO)

# EN CONSTRUCCIÓN...

def mostrar_dato(etiqueta: str | int | float | None = "", valor: str | int | float | None = ""):
    # 1. Normalizar si vienen como None
    if etiqueta is None:
        etiqueta = ""
    if valor is None:
        valor = ""

    # 2. Convertir a string de forma segura
    etiqueta_str = str(etiqueta)
    valor_str = str(valor)

    # 3. Si no hay valor (es un texto vacío), muestra solo la etiqueta sin los dos puntos ":"
    if not valor_str:
        print(f"  ► {etiqueta_str}")
    else:
        print(f"  ► {etiqueta_str:<15}: {valor_str:>10}")