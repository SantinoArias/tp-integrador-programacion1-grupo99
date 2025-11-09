<div align="center">

# TP Integrador — Programación 1  
### Gestión de Países (Python · App de consola)

**Cargar, validar y analizar un CSV de países con búsquedas, filtros, ordenamientos y estadísticas.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)]()
[![CLI](https://img.shields.io/badge/Interface-CLI-222)]()
[![Status](https://img.shields.io/badge/Estado-Listo%20para%20entregar-22c55e)]()

</div>

---

## 🧭 Tabla de contenidos
- [¿Qué es?](#-qué-es)
- [Cómo funciona](#-cómo-funciona)
- [Requisitos](#-requisitos)
- [Ejecución rápida](#-ejecución-rápida)
- [Formato del CSV](#-formato-del-csv)
- [Flujo](#-flujo)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Integrantes](#-integrantes)

---

## 💡 ¿Qué es?
Aplicación de **consola** hecha en **Python 3** que opera sobre un dataset de países (CSV).  
Permite **buscar** por nombre, **filtrar** por continente y rangos, **ordenar** por varios criterios y obtener **estadísticas**.

### Funcionalidades (resumen)
| 🔎 Búsqueda | 🔧 Filtros | ↕ Ordenamiento | 📊 Estadísticas | ✅ Validaciones | 🧪 (Opc.) Tests |
|---|---|---|---|---|---|
| Exacta/parcial (case-insensitive) | Continente · Población · Superficie | Nombre · Población · Superficie (asc/desc) | Mayor/menor · Promedios · Conteo por continente | Columnas, tipos y rangos con mensajes claros | `pytest` para lógica y CSV |

---

## ⚙️ Cómo funciona
1. **Carga el CSV** (valida columnas, tipos y rangos; maneja `utf-8/utf-8-sig`).
2. Muestra un **menú** de opciones:
   - **Buscar** por nombre (coincidencia parcial).
   - **Filtrar** por continente y/o por rangos numéricos.
   - **Ordenar** por nombre, población o superficie (asc/desc).
   - **Estadísticas** (mayor/menor, promedios, conteo por continente).
   - **Agregar/actualizar** país (opcional) y **guardar** (opcional).
3. Imprime **resultados y mensajes claros** en consola.

---

## 🧩 Requisitos
- **Python 3.10+**
- Un archivo CSV con encabezados:  
  `nombre,poblacion,superficie,continente`

