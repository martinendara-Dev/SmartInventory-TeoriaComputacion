"""Diez correos: búsqueda exacta y verificadores independientes de la búsqueda.

Una entrada mal formada genera ValueError. Un certificado incorrecto devuelve
False. Las búsquedas exhaustivas son solo para instancias pequeñas.
"""
from collections import deque
from itertools import permutations, product
from .logistica import entero, validar_grafo


def alcanzable(grafo, origen, destino):
    validar_grafo(grafo)
    if origen not in grafo or destino not in grafo:
        raise ValueError("Nodo inexistente")
    visitados = {origen}
    pendientes = deque([origen])
    while pendientes:
        actual = pendientes.popleft()
        if actual == destino:
            return True
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                pendientes.append(vecino)
    return False


def flujo_maximo(capacidades, origen, destino):
    """Edmonds–Karp. Devuelve flujo y registro de cada camino aumentante."""
    validar_grafo(capacidades)
    if origen not in capacidades or destino not in capacidades or origen == destino:
        raise ValueError("Se requieren dos nodos existentes y distintos")
    residual = {u: dict(vecinos) for u, vecinos in capacidades.items()}
    for u, vecinos in capacidades.items():
        for v in vecinos:
            residual[v].setdefault(u, 0)
    total = 0
    pasos = []
    while True:
        anterior = {origen: None}
        pendientes = deque([origen])
        while pendientes and destino not in anterior:
            actual = pendientes.popleft()
            for vecino, capacidad in residual[actual].items():
                if capacidad > 0 and vecino not in anterior:
                    anterior[vecino] = actual
                    pendientes.append(vecino)
        if destino not in anterior:
            return total, pasos
        camino = [destino]
        aumento = float("inf")
        v = destino
        while v != origen:
            u = anterior[v]
            aumento = min(aumento, residual[u][v])
            camino.append(u)
            v = u
        cambios = []
        v = destino
        while v != origen:
            u = anterior[v]
            residual[u][v] -= aumento
            residual[v][u] += aumento
            cambios.append((u, v, residual[u][v], residual[v][u]))
            v = u
        total += aumento
        pasos.append({"camino": list(reversed(camino)), "aumento": aumento,
                      "total": total, "residuales": list(reversed(cambios))})


def matriz_adyacencia(matriz):
    if not isinstance(matriz, (list, tuple)):
        raise ValueError("Se requiere una matriz")
    n = len(matriz)
    if any(not isinstance(fila, (list, tuple)) or len(fila) != n for fila in matriz):
        raise ValueError("La matriz debe ser cuadrada")
    if any(type(x) is not int or x not in (0, 1) for fila in matriz for x in fila):
        raise ValueError("La adyacencia solo admite 0 y 1")
    if any(matriz[i][i] != 0 for i in range(n)):
        raise ValueError("El modelo no incluye lazos")
    if any(matriz[i][j] != matriz[j][i] for i in range(n) for j in range(n)):
        raise ValueError("La red debe ser no dirigida")


def _permutacion_valida(certificado, n):
    return (isinstance(certificado, (tuple, list)) and len(certificado) == n
            and all(type(i) is int for i in certificado)
            and set(certificado) == set(range(n)))


def _conserva_aristas(red_a, red_b, certificado):
    return all(red_a[i][j] == red_b[certificado[i]][certificado[j]]
               for i in range(len(red_a)) for j in range(len(red_a)))


def verificar_isomorfismo(red_a, red_b, certificado):
    matriz_adyacencia(red_a)
    matriz_adyacencia(red_b)
    n = len(red_a)
    return (len(red_b) == n and _permutacion_valida(certificado, n)
            and _conserva_aristas(red_a, red_b, certificado))


def buscar_isomorfismo(red_a, red_b):
    matriz_adyacencia(red_a)
    matriz_adyacencia(red_b)
    if len(red_a) != len(red_b):
        return None
    for certificado in permutations(range(len(red_a))):
        if _conserva_aristas(red_a, red_b, certificado):
            return certificado
    return None


def verificar_factor(numero, limite, divisor):
    entero(numero, "numero", 2)
    entero(limite, "limite")
    return type(divisor) is int and 2 <= divisor <= limite and numero % divisor == 0


def buscar_factor(numero, limite):
    entero(numero, "numero", 2)
    entero(limite, "limite")
    # Divisores mayores que N son imposibles. El enunciado sí permite d = N.
    for divisor in range(2, min(limite, numero) + 1):
        if numero % divisor == 0:
            return divisor
    return None


def validar_modular(modulo, base, objetivo, limite):
    entero(modulo, "modulo", 2)
    entero(base, "base", 1)
    entero(objetivo, "objetivo")
    entero(limite, "limite")
    if base >= modulo or objetivo >= modulo:
        raise ValueError("Base y objetivo deben ser menores que el módulo")
    # El expediente garantiza p primo. Estas operaciones también funcionan para
    # otros módulos; no se presenta esta validación como una prueba de primalidad.


def verificar_exponente(modulo, base, objetivo, limite, exponente):
    validar_modular(modulo, base, objetivo, limite)
    return (type(exponente) is int and 0 <= exponente <= limite
            and pow(base, exponente, modulo) == objetivo)


def buscar_exponente(modulo, base, objetivo, limite):
    validar_modular(modulo, base, objetivo, limite)
    valor = 1
    for exponente in range(limite + 1):
        if valor == objetivo:
            return exponente
        valor = valor * base % modulo
    return None


def verificar_automorfismo(red, certificado):
    return (verificar_isomorfismo(red, red, certificado)
            and tuple(certificado) != tuple(range(len(red))))


def buscar_automorfismo(red):
    matriz_adyacencia(red)
    identidad = tuple(range(len(red)))
    for certificado in permutations(identidad):
        if certificado != identidad and _conserva_aristas(red, red, certificado):
            return certificado
    return None


def validar_formula(clausulas, variables):
    entero(variables, "variables")
    if not isinstance(clausulas, (tuple, list)):
        raise ValueError("Se requiere una lista de cláusulas")
    for clausula in clausulas:
        if not isinstance(clausula, (list, tuple)) or not 1 <= len(clausula) <= 3:
            raise ValueError("Cada cláusula tiene entre 1 y 3 literales")
        if any(type(x) is not int or not 1 <= abs(x) <= variables for x in clausula):
            raise ValueError("Literal fuera del rango de variables")


def _satisface(clausulas, asignacion):
    return all(any(asignacion[abs(literal) - 1] == (literal > 0)
                   for literal in clausula) for clausula in clausulas)


def verificar_sat(clausulas, variables, asignacion):
    validar_formula(clausulas, variables)
    return (isinstance(asignacion, (list, tuple)) and len(asignacion) == variables
            and all(type(x) is bool for x in asignacion)
            and _satisface(clausulas, asignacion))


def buscar_sat(clausulas, variables):
    validar_formula(clausulas, variables)
    for asignacion in product((False, True), repeat=variables):
        if _satisface(clausulas, asignacion):
            return asignacion
    return None


def validar_distancias(distancias, limite):
    entero(limite, "limite")
    if not isinstance(distancias, (list, tuple)) or not distancias:
        raise ValueError("Se requiere al menos un centro")
    n = len(distancias)
    for i, fila in enumerate(distancias):
        if not isinstance(fila, (list, tuple)) or len(fila) != n:
            raise ValueError("La matriz de distancias debe ser cuadrada")
        for valor in fila:
            entero(valor, "distancia")
        if fila[i] != 0:
            raise ValueError("La diagonal debe ser cero")


def verificar_tsp(distancias, limite, ruta):
    validar_distancias(distancias, limite)
    n = len(distancias)
    if not isinstance(ruta, (list, tuple)) or len(ruta) != n + 1:
        return False
    if not _permutacion_valida(ruta[:-1], n) or type(ruta[-1]) is not int:
        return False
    return (ruta[0] == ruta[-1] == 0
            and sum(distancias[ruta[i]][ruta[i+1]] for i in range(n)) <= limite)


def buscar_tsp(distancias, limite):
    validar_distancias(distancias, limite)
    n = len(distancias)
    for orden in permutations(range(1, n)):
        ruta = (0,) + orden + (0,)
        costo = sum(distancias[ruta[i]][ruta[i+1]] for i in range(n))
        if costo <= limite:
            return ruta, costo  # Primera solución válida. No promete la óptima.
    return None


def validar_cobertura(grafo, limite):
    validar_grafo(grafo)
    entero(limite, "limite")
    if any(u == v or u not in grafo[v] for u in grafo for v in grafo[u]):
        raise ValueError("Se requiere grafo no dirigido, sin lazos")


def _cubre_aristas(grafo, elegidos):
    return all(u in elegidos or v in elegidos for u in grafo for v in grafo[u])


def verificar_cobertura(grafo, limite, certificado):
    validar_cobertura(grafo, limite)
    if not isinstance(certificado, (list, tuple, set)):
        return False
    if any(type(u) is not str for u in certificado):
        return False
    elegidos = set(certificado)
    return (len(elegidos) == len(certificado) and len(elegidos) <= limite
            and elegidos <= grafo.keys() and _cubre_aristas(grafo, elegidos))


def buscar_cobertura(grafo, limite):
    validar_cobertura(grafo, limite)
    vertices = list(grafo)
    for mascara in range(1 << len(vertices)):
        if mascara.bit_count() > limite:
            continue
        elegidos = {vertices[i] for i in range(len(vertices)) if mascara & (1 << i)}
        if _cubre_aristas(grafo, elegidos):
            return sorted(elegidos)
    return None
