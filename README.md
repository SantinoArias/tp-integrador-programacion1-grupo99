<div align="center">

# TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN (A DISTANCIA)
### 3 — Programación 1  
# TP Integrador — Gestión de Países (Python · App de consola)

**Cargar, validar y analizar un CSV de países con búsquedas, filtros, ordenamientos y estadísticas.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)]()
[![CLI](https://img.shields.io/badge/Interface-CLI-222)]()
[![Status](https://img.shields.io/badge/Estado-Listo%20para%20entregar-22c55e)]()

</div>

---

## 🧭 Tabla de contenidos
- [Descripción del programa](#-descripción-del-programa)
- [Instrucciones de uso](#-instrucciones-de-uso)
- [Ejemplos de entradas y salidas](#-ejemplos-de-entradas-y-salidas)
- [Requisitos](#-requisitos)
- [Ejecución rápida](#-ejecución-rápida)
- [Formato del CSV](#-formato-del-csv)
- [Flujo](#-flujo)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Participación de los integrantes](#-participación-de-los-integrantes)

---

## 💡 Descripción del programa
Aplicación de **consola** hecha en **Python 3** que opera sobre un dataset de países (CSV).  
Permite **buscar** por nombre, **filtrar** por continente y rangos, **ordenar** por varios criterios y obtener **estadísticas**.

### Funcionalidades (resumen)
| 🔎 Búsqueda | 🔧 Filtros | ↕ Ordenamiento | 📊 Estadísticas | ✅ Validaciones |
|---|---|---|---|---|
| Exacta/parcial (case-insensitive) | Continente · Población · Superficie | Nombre · Población · Superficie (asc/desc) | Mayor/menor · Promedios · Conteo por continente | Columnas, tipos y rangos con mensajes claros |

---

## 🛠️ Instrucciones de uso
1. **Clonar** el repositorio y verificar **Python 3.10+** instalado.  
2. Ubicar un dataset CSV con encabezados: `nombre,poblacion,superficie,continente`.  
3. **Ejecutar** la app desde la raíz del proyecto con el parámetro `--dataset`:
   - **Windows (PowerShell/CMD)**  
     ```powershell
     python -m src.cli --dataset ".\data\paises.csv"
     ```
   - **Linux / macOS**  
     ```bash
     python3 -m src.cli --dataset "./data/paises.csv"
     ```


**Menú principal**
1) Buscar por nombre (parcial/exacto)  
2) Filtrar por continente  
3) Filtrar por rango de población  
4) Filtrar por rango de superficie  
5) Ordenar (nombre/población/superficie; asc/desc)  
6) Estadísticas del dataset  
7) Salir

---

## 🧪 Ejemplos de entradas y salidas

**Ejemplo 1 — Búsqueda parcial**
```
> Opción: 1
Ingrese nombre o parte: arg
Resultados:
- Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
```

**Ejemplo 2 — Filtro por continente**
```
> Opción: 2
Ingrese continente: América
Coincidencias (5):
- Argentina ...
- Brasil ...
- Chile ...
- Colombia ...
- México ...
```

**Ejemplo 3 — Filtro por rango de población**
```
> Opción: 3
Población mínima: 50000000
Población máxima: 300000000
Resultados (3):
- Italia: 60317116
- México: 126014024
- Brasil: 212559417
```

**Ejemplo 4 — Ordenar por superficie (desc)**
```
> Opción: 5
Campo a ordenar [nombre/poblacion/superficie]: superficie
Dirección [asc/desc]: desc
Top 5:
1) Rusia - 17098242
2) Canadá - 9984670
3) Estados Unidos - 9833517
4) China - 9596961
5) Brasil - 8515767
```

**Ejemplo 5 — Estadísticas**
```
> Opción: 6
Mayor población: India (1428627663)
Menor población: Nauru (12580)
Promedio población: 195.3 millones
Promedio superficie: 1.23 millones km²
Países por continente: América=35 | Europa=44 | África=54 | Asia=49 | Oceanía=14
```

**Ejemplo 6 — Validación de entrada**
```
> Opción: 3
Población mínima: abc
[Error] Ingresá un número entero válido.
```

> Nota: Los datos y cantidades son ilustrativos; los resultados reales dependen del CSV.

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
MENÚ (Buscar / Filtrar / Ordenar / Estadísticas)
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

## 👥 Participación de los integrantes
| Integrante        | Rol / Actividad principal                         | % de aporte |
|-------------------|---------------------------------------------------|------------:|
| **Santino Arias** | Desarrollo, pruebas, documentación y video        | **100%**    |

> Declaración: esta tabla refleja la participación real en la entrega actual.
