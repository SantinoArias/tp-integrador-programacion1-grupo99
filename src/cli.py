# ===============================================
# TP Integrador - Programación 1
# Módulo: CLI (interfaz de consola)
# Autor: Santino Arias
# Nota: Solo agrego COMENTARIOS para explicar decisiones.
#       No modifiqué ninguna línea de lógica/código existente.
# ===============================================

from __future__ import annotations
import argparse
import sys
from typing import List, Optional, Tuple

# Importo utilidades de IO (CSV) y el núcleo de negocio.
# CSVInvalido es mi excepción personalizada para errores de formato.
from .io_utils import cargar_paises, guardar_paises, CSVInvalido
from .core import (
    agregar_pais, actualizar_pais,
    buscar_por_nombre, filtrar_por_continente,
    filtrar_por_rango_poblacion, filtrar_por_rango_superficie,
    ordenar, estadisticas, Pais
)


def imprimir_paises(paises: List[Pais], max_rows: int = 30) -> None:
    """Salida tabulada sencilla (sin libs externas)."""
    # Si la lista viene vacía, informo y retorno.
    if not paises:
        print("No hay resultados.")
        return
    # Calculo anchos de columnas para alinear salida en consola.
    colw = {
        "nombre": max(6, max((len(p["nombre"]) for p in paises), default=6)),
        "poblacion": 10,
        "superficie": 10,
        "continente": max(10, max((len(p["continente"]) for p in paises), default=10)),
    }
    header = f"{'Nombre':<{colw['nombre']}}  {'Población':>{colw['poblacion']}}  {'Superficie':>{colw['superficie']}}  {'Continente':<{colw['continente']}}"
    print(header)
    print("-" * len(header))
    # Imprimo hasta max_rows filas para evitar salidas interminables.
    for i, p in enumerate(paises):
        if i >= max_rows:
            restantes = len(paises) - max_rows
            print(f"... ({restantes} más)")
            break
        print(
            f"{p['nombre']:<{colw['nombre']}}  "
            f"{p['poblacion']:>{colw['poblacion']},}  "
            f"{p['superficie']:>{colw['superficie']},}  "
            f"{p['continente']:<{colw['continente']}}"
        )


def _leer_entero(msg: str) -> Optional[int]:
    # Leo un entero opcional desde teclado.
    # Si la persona aprieta Enter, retorno None para “omitir” el valor.
    s = input(msg).strip()
    if s == "":
        return None
    try:
        return int(s)
    except ValueError:
        print("Ingresá un número entero válido.")
        return None


def _leer_rango_int(msg_min: str, msg_max: str) -> Tuple[Optional[int], Optional[int], bool]:
    """Devuelve (min, max, hubo_error). Enter para omitir un extremo."""
    # Acepto mínimo y máximo como opcionales; si ambos están y min>max, marco error.
    min_s = input(msg_min).strip()
    max_s = input(msg_max).strip()
    try:
        min_v = int(min_s) if min_s else None
        max_v = int(max_s) if max_s else None
    except ValueError:
        print("Ingresá números enteros (o Enter para omitir)." )
        return None, None, True
    if min_v is not None and max_v is not None and min_v > max_v:
        print("Rango inválido: el mínimo no puede ser mayor que el máximo.")
        return None, None, True
    return min_v, max_v, False


def menu(paises: List[Pais], ruta_csv: str) -> None:
    # Flag para saber si hay cambios sin persistir en disco.
    dirty = False  # hay cambios sin guardar

    while True:
        # Menú textual simple. Mantengo opciones numeradas para facilitar las pruebas.
        print("\n=== Menú ===")
        print("1) Agregar país")
        print("2) Actualizar país (población y/o superficie)")
        print("3) Buscar por nombre (parcial o exacto)")
        print("4) Filtrar por continente")
        print("5) Filtrar por rango de población")
        print("6) Filtrar por rango de superficie")
        print("7) Ordenar")
        print("8) Estadísticas")
        print("9) Guardar cambios")
        print("0) Salir")
        op = input("Opción: ").strip()

        try:
            if op == "0":
                # Al salir, si hay cambios pendientes, pregunto si guardo.
                if dirty:
                    resp = input("Hay cambios sin guardar. ¿Guardar ahora? [s/N]: ").strip().lower()
                    if resp == "s":
                        guardar_paises(ruta_csv, paises)
                        print(f"Cambios guardados en {ruta_csv}.")
                    else:
                        print("Saliendo sin guardar cambios…")
                print("Hasta luego.")
                break

            elif op == "9":
                # Persisto en disco la lista actual (sobrescribe el CSV de origen de forma atómica).
                guardar_paises(ruta_csv, paises)
                dirty = False
                print(f"Cambios guardados en {ruta_csv}.")

            elif op == "1":
                # Alta de país: todos los campos obligatorios.
                nombre = input("Nombre: ").strip()
                poblacion = _leer_entero("Población: ")
                superficie = _leer_entero("Superficie (km²): ")
                continente = input("Continente: ").strip()
                if poblacion is None or superficie is None:
                    print("Operación cancelada (valores inválidos)." )
                    continue
                agregar_pais(paises, nombre, poblacion, superficie, continente)
                dirty = True
                print("País agregado con éxito.")

            elif op == "2":
                # Actualización parcial: permito omitir población o superficie.
                nombre = input("Nombre del país a actualizar: ").strip()
                p = input("Nueva población (Enter para omitir): ").strip()
                s = input("Nueva superficie (km², Enter para omitir): ").strip()
                nueva_p = int(p) if p else None
                nueva_s = int(s) if s else None
                res = actualizar_pais(paises, nombre, nueva_p, nueva_s)
                if res is None:
                    print("No se encontró un país con ese nombre (recordá que se ignoran tildes/mayúsculas)." )
                else:
                    dirty = True
                    print("País actualizado con éxito.")

            elif op == "3":
                # Búsqueda exacta o parcial (case-insensitive, sin tildes).
                patron = input("Texto a buscar (se ignoran tildes y mayúsculas): ").strip()
                exacto = input("¿Búsqueda exacta? [s/N]: ").strip().lower() == "s"
                encontrados = buscar_por_nombre(paises, patron, exacto=exacto)
                imprimir_paises(encontrados)

            elif op == "4":
                # Filtro por continente (normalización en core).
                cont = input("Continente: ").strip()
                imprimir_paises(filtrar_por_continente(paises, cont))

            elif op == "5":
                # Filtro por rango de población, tolerando extremos omitidos.
                min_p, max_p, err = _leer_rango_int("Población mínima (Enter para omitir): ",
                                                    "Población máxima (Enter para omitir): ")
                if err: 
                    continue
                imprimir_paises(filtrar_por_rango_poblacion(paises, min_p, max_p))

            elif op == "6":
                # Filtro por rango de superficie, con misma política que población.
                min_s, max_s, err = _leer_rango_int("Superficie mínima (Enter para omitir): ",
                                                    "Superficie máxima (Enter para omitir): ")
                if err:
                    continue
                imprimir_paises(filtrar_por_rango_superficie(paises, min_s, max_s))

            elif op == "7":
                # Orden genérico por clave, asc/desc. Valido la clave en core.
                clave = input("Ordenar por (nombre | poblacion | superficie): ").strip().lower()
                desc = input("¿Descendente? [s/N]: ").strip().lower() == "s"
                imprimir_paises(ordenar(paises, clave, descendente=desc))

            elif op == "8":
                # Muestro estadísticas consolidadas (mayor/menor, promedios y conteo por continente).
                s = estadisticas(paises)
                print("\n> Estadísticas")
                if s["n"] == 0:
                    print("- Sin datos.")
                else:
                    may = s["mayor_poblacion"]; men = s["menor_poblacion"]
                    print(f"- Países considerados: {s['n']}")
                    print(f"- Mayor población: {may['nombre']} ({may['poblacion']:,})")
                    print(f"- Menor población: {men['nombre']} ({men['poblacion']:,})")
                    print(f"- Promedio de población: {int(s['prom_poblacion']):,}")
                    print(f"- Promedio de superficie: {int(s['prom_superficie']):,} km²")
                    print("- Cantidad por continente:")
                    for c, n in s['cant_por_continente'].items():
                        print(f"  * {c}: {n}")

            else:
                # Opción fuera de rango.
                print("Opción inválida.")
        except ValueError as e:
            # Errores de validación esperables (flujos normales).
            print(f"Error: {e}")
        except Exception as e:
            # Cualquier excepción no prevista la informo por stderr para distinguirla.
            print(f"Error inesperado: {e}", file=sys.stderr)


def main(argv: Optional[List[str]] = None) -> int:
    # Uso argparse para permitir pasar el CSV por parámetro (--dataset).
    parser = argparse.ArgumentParser(description="Gestión de países (CSV)." )
    parser.add_argument("--dataset", "-d", required=True, help="Ruta al CSV")
    args = parser.parse_args(argv)

    try:
        # Cargo el CSV y construyo la lista de dicts (ver io_utils.cargar_paises).
        paises = cargar_paises(args.dataset)
    except (FileNotFoundError, CSVInvalido) as e:
        # Errores “controlados” de carga: informo por stderr y devuelvo código 2.
        print(f"Error al cargar el CSV: {e}", file=sys.stderr)
        return 2
    except Exception as e:
        # Cualquier otro error de inicio lo marco como 3 (genérico).
        print(f"Error inesperado: {e}", file=sys.stderr)
        return 3

    print(f"Cargados {len(paises)} países desde {args.dataset}")
    menu(paises, args.dataset)
    return 0


if __name__ == "__main__":
    # main como punto de entrada del módulo ejecutado (python -m src.cli)
    raise SystemExit(main())
