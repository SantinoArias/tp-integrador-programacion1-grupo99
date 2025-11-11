from __future__ import annotations
from typing import List, Dict, Any, Tuple
import csv
import os
import sys

# Estructura compatible con core.Pais (mantengo Dict[str, Any] aquí para no ciclar importaciones).
Pais = Dict[str, Any]
# Defino el orden y los nombres canónicos de las columnas que espero.
CAMPOS_REQUERIDOS = ("nombre", "poblacion", "superficie", "continente")


class CSVInvalido(Exception):
    """Error de formato/validación del CSV."""


def _mapear_headers(headers: List[str]) -> Dict[str, str]:
    """
    Permite headers flexibles. Devuelve un mapa header_origen -> header_canonico.
    Idea: aceptar variantes comunes (p. ej. 'hab', 'population', 'km2') para no romper la carga.
    """
    canonicos = {
        "nombre": {"nombre", "pais", "country"},
        "poblacion": {"poblacion", "población", "population", "hab", "habitantes"},
        "superficie": {"superficie", "area", "área", "km2", "km^2"},
        "continente": {"continente", "region", "región", "continent"},
    }
    mapa: Dict[str, str] = {}
    for h in headers:
        h_low = h.strip().lower()
        asignado = False
        for canon, variantes in canonicos.items():
            if h_low in variantes:
                mapa[h] = canon
                asignado = True
                break
        if not asignado:
            # Si no lo pude mapear por variantes, pruebo si coincide con algún canónico exacto.
            if h_low in canonicos:
                mapa[h] = h_low
    return mapa


def _to_int(value: Any, campo: str, fila_nro: int) -> int:
    # Convierto valores “numéricos” tolerando separadores de miles como puntos/espacios/comas.
    s = str(value).strip()
    if s == "":
        raise CSVInvalido(f"Fila {fila_nro}: campo '{campo}' vacío.")
    # Eliminar separadores de miles comunes dejando solo dígitos.
    s_limpio = "".join(ch for ch in s if ch.isdigit())
    if s_limpio == "":
        raise CSVInvalido(f"Fila {fila_nro}: campo '{campo}' no es numérico: {value!r}")
    return int(s_limpio)


def cargar_paises(ruta_csv: str) -> List[Pais]:
    """
    Lee el CSV, valida y convierte tipos. Tolera filas con errores (avisa por stderr).
    Si una fila está mal, la salto y sigo con el resto (no detengo toda la carga).
    """
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(ruta_csv)

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise CSVInvalido("El CSV no tiene encabezados.")
        # Mapeo headers de origen a nombres canónicos y verifico que estén todos.
        mapa = _mapear_headers(reader.fieldnames)
        faltantes = set(CAMPOS_REQUERIDOS) - set(mapa.values())
        if faltantes:
            raise CSVInvalido(f"Headers faltantes: {', '.join(sorted(faltantes))}")

        out: List[Pais] = []
        # i arranca en 2 porque la fila 1 es el encabezado.
        for i, row in enumerate(reader, start=2):  # datos arrancan en fila 2 (tras encabezados)
            try:
                # Obtengo cada campo buscando la clave original cuyo canónico sea el requerido.
                nombre = str(row.get(next(k for k, v in mapa.items() if v == 'nombre'), "")).strip()
                continente = str(row.get(next(k for k, v in mapa.items() if v == 'continente'), "")).strip()
                poblacion_raw = row.get(next(k for k, v in mapa.items() if v == 'poblacion'), "")
                superficie_raw = row.get(next(k for k, v in mapa.items() if v == 'superficie'), "")

                if not nombre or not continente:
                    # Exijo al menos nombre y continente no vacíos.
                    raise CSVInvalido(f"Fila {i}: nombre/continente vacío.")

                # Convierto a int tolerando separadores (ver _to_int).
                poblacion = _to_int(poblacion_raw, "poblacion", i)
                superficie = _to_int(superficie_raw, "superficie", i)

                # Agrego el país ya normalizado de tipos.
                out.append({
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente,
                })
            except Exception as e:
                # Reporto advertencia por stderr y continúo (no freno toda la carga).
                print(f"[Advertencia] {e}", file=sys.stderr)
                continue

    return out


def guardar_paises(ruta_csv: str, paises: List[Pais]) -> None:
    # Escritura “atómica”: primero escribo a .tmp y luego reemplazo el CSV original.
    tmp = ruta_csv + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(CAMPOS_REQUERIDOS))
        writer.writeheader()
        for p in paises:
            writer.writerow({
                "nombre": p["nombre"],
                "poblacion": int(p["poblacion"]),
                "superficie": int(p["superficie"]),
                "continente": p["continente"],
            })
    os.replace(tmp, ruta_csv)


# Alias por si quedó otro nombre escrito en algún lado (retrocompatibilidad mínima).
def carga_paises(ruta_csv: str) -> List[Pais]:
    return cargar_paises(ruta_csv)


__all__ = ["cargar_paises", "carga_paises", "guardar_paises", "CSVInvalido"]
