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
| 🔎 Búsqueda | 🔧 Filtros | ↕ Ordenamiento | 📊 Estadísticas | ✅ Validaciones |
|---|---|---|---|---|
| Exacta/parcial (case-insensitive) | Continente · Población · Superficie | Nombre · Población · Superficie (asc/desc) | Mayor/menor · Promedios · Conteo por continente | Columnas, tipos y rangos con mensajes claros |

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

---

## ▶️ Ejecución rápida
**Windows (PowerShell)**
```powershell
python -m src.cli --dataset ".\data\paises.csv"
```

**Linux/Mac**
```bash
python3 -m src.cli --dataset "./data/paises.csv"
```

> Si tu CSV viene de Excel con BOM, podés agregar: `--encoding utf-8-sig`.

---

## 📄 Formato del CSV
```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Chile,19116209,756102,América
España,47351567,505990,Europa
Nigeria,206139589,923768,África
```
- `poblacion >= 0` · `superficie > 0` · separador **coma** · encoding **UTF-8**.

---

## 🗺️ Flujo
```
INICIO
  ↓
Cargar CSV → validar → construir lista de países
  ↓
MENÚ (Buscar / Filtrar / Ordenar / Estadísticas / Agregar-Actualizar)
  ↓
Mostrar resultados → Volver al MENÚ → Salir
```

---

## 🗂️ Estructura del proyecto
```
tp-integrador/
├─ src/
│  ├─ core.py        # búsquedas, filtros, ordenamientos, estadísticas
│  ├─ io_utils.py    # lectura CSV, parsing y validaciones
│  └─ cli.py         # interfaz de consola y orquestación
├─ data/
│  └─ paises.csv     # dataset de ejemplo
└─ README.md
```

---

## 👥 Integrantes
- Apellido, Nombre — Legajo  
- Apellido, Nombre — Legajo
