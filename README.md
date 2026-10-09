# 📦 Sistema de Gestión de Inventario (Listas + Tuplas)

Proyecto de práctica modular para dominar la manipulación de listas, tuplas, slicing y formateo de consola en Python.

> **Nota de arquitectura:** El código está estructurado de forma modular (utilizando `interfaz.py` y archivos por nivel). Algunas funciones del enunciado oficial fueron unificadas y optimizadas para evitar redundancias y mantener un flujo de programa fluido.

---

## 📋 Módulos y Cobertura Técnica

### Nivel 1: Fundamentos
- Creación e inicialización del inventario base.
- Recorrido iterativo con desempaquetado de tuplas.
- Acceso por índices (`0`, `-1`) y cálculo de tamaño con `len()`.

### Nivel 2: Manipulación Avanzada
- Inserción y expansión masiva de elementos mediante `.extend()`, `.append()` e `.insert()`.
- Eliminación de elementos con `.remove()` y retención/retorno con `.pop()`.
- Segmentación de listas mediante *slicing* (`[:3]`, `[1:-1]`, `[::-1]`).

### Nivel 3: Algoritmos y Transformaciones
- Filtrado y extracción de datos mediante *List Comprehension*.
- Cálculo de impuestos (IVA 19%) sobre colecciones.
- Ordenamiento y búsqueda de extremos (`max`, `sorted`) utilizando `key=lambda x: x[1]`.

### Nivel 4: Integración y Reportes
- Buscador de productos con retorno seguro (`None`).
- Generación de reportes unificados con resúmenes estadísticos (totales, promedio, extremos).
- Transformación masiva con porcentajes de descuento.