# TP Integrador – Programación 1
**Gestión de Países en Python (app de consola)**

## ¿Qué es?
Una aplicación de **consola** hecha en **Python 3** que carga un **dataset de países** desde un archivo **CSV** y permite:
- **Buscar** por nombre (coincidencia exacta o parcial).
- **Filtrar** por **continente** y por rangos de **población** y **superficie**.
- **Ordenar** por **nombre**, **población** o **superficie** (asc/desc).
- Ver **estadísticas**: mayor/menor población, promedios y cantidad de países por continente.

> Pensado como trabajo integrador para practicar **listas, diccionarios, funciones, condicionales, archivos CSV y ordenamientos**.

---

## ¿Cómo funciona?
1. **Carga el CSV** (valida columnas, tipos y rangos).
2. Muestra un **menú** para operar sobre el dataset:
   - **Buscar** por nombre (no distingue mayúsculas/minúsculas).
   - **Filtrar** por continente y/o por rangos numéricos.
   - **Ordenar** por el campo elegido, ascendente o descendente.
   - **Estadísticas** con resultados claros.
   - **Agregar/actualizar** un país (opcional).
   - **Guardar cambios** (opcional) o **Salir**.
3. Los resultados se imprimen en consola con **mensajes claros** (si hay errores o no hay resultados, también te lo avisa).

---

## Requisitos
- **Python 3.10+**
- Un archivo CSV con estas columnas (en este orden): nombre,poblacion,superficie,continente

