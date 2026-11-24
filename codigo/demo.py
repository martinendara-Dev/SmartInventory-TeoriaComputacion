"""Demostración reproducible. Ejecutar desde la raíz: python -m codigo.demo."""
from pathlib import Path
import json
from .logistica import dijkstra, ruta_minima, fefo, reposicion
from .correos import (alcanzable, flujo_maximo, buscar_isomorfismo,
    verificar_isomorfismo, buscar_factor, verificar_factor, buscar_exponente,
    verificar_exponente, buscar_automorfismo, verificar_automorfismo,
    buscar_sat, verificar_sat, buscar_tsp, verificar_tsp,
    buscar_cobertura, verificar_cobertura)

BASE = Path(__file__).resolve().parents[1]


def resultados():
    planta = json.loads((BASE / 'datos/planta.json').read_text(encoding='utf-8'))
    red = {'Durán': {'Quito': 1, 'Guayaquil': 1}, 'Quito': {'Norte': 1},
           'Guayaquil': {'Sur': 1}, 'Norte': {}, 'Sur': {}}
    tiempos = {'Quito': {'Latacunga': 2, 'Ambato': 5},
               'Latacunga': {'Guayaquil': 6}, 'Ambato': {'Guayaquil': 3}, 'Guayaquil': {}}
    capacidades = {'Planta': {'Quito': 7, 'Guayaquil': 5},
                   'Quito': {'Clientes': 4, 'Guayaquil': 2},
                   'Guayaquil': {'Clientes': 6}, 'Clientes': {}}
    red_a = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    red_b = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    triangulo = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    clausulas = [[1, -2], [2, 3]]
    distancias = [[0, 4, 8], [4, 0, 3], [8, 3, 0]]
    corredores = {'A': {'B': 1}, 'B': {'A': 1, 'C': 1}, 'C': {'B': 1}}
    iso = buscar_isomorfismo(red_a, red_b)
    factor = buscar_factor(91, 10)
    exponente = buscar_exponente(23, 5, 8, 10)
    auto = buscar_automorfismo(triangulo)
    sat = buscar_sat(clausulas, 3)
    tsp = buscar_tsp(distancias, 20)
    cobertura = buscar_cobertura(corredores, 1)
    lotes = [('A02', '30/11/2026', 4), ('A01', '30/11/2026', 3),
             ('B01', '03/12/2026', 5), ('V01', '23/11/2026', 9), ('C00', '01/12/2026', 0)]
    return {
        'planta': ruta_minima(planta['grafo'], 'R', 'D'),
        'fefo': fefo(lotes, 8, '24/11/2026'),
        'reposicion': reposicion(18, 10, 5, 30, 50),
        'reposicion_tras_orden': reposicion(18, 37, 5, 30, 50),
        'p1': alcanzable(red, 'Durán', 'Norte'),
        'p2': {'distancias': dijkstra(tiempos, 'Quito')[0],
               'ruta': ruta_minima(tiempos, 'Quito', 'Guayaquil')},
        'p3': flujo_maximo(capacidades, 'Planta', 'Clientes'),
        'n1': {'certificado': iso, 'verificado': verificar_isomorfismo(red_a, red_b, iso)},
        'n2': {'certificado': factor, 'verificado': verificar_factor(91, 10, factor)},
        'n3': {'certificado': exponente, 'verificado': verificar_exponente(23, 5, 8, 10, exponente)},
        'n4': {'certificado': auto, 'verificado': verificar_automorfismo(triangulo, auto)},
        'c1': {'certificado': sat, 'verificado': verificar_sat(clausulas, 3, sat)},
        'c2': {'certificado': tsp, 'verificado': verificar_tsp(distancias, 20, tsp[0])},
        'c3': {'certificado': cobertura, 'verificado': verificar_cobertura(corredores, 1, cobertura)}
    }


def main():
    print(json.dumps(resultados(), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
