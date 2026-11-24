"""Rutas e inventario. No lee archivos, no imprime ni modifica las entradas."""
from datetime import datetime
import heapq


def entero(valor, nombre, minimo=0):
    if type(valor) is not int or valor < minimo:
        raise ValueError(f"{nombre} debe ser entero >= {minimo}")


def validar_grafo(grafo):
    """Grafo simple dirigido: {nombre: {vecino: peso entero no negativo}}."""
    if not isinstance(grafo, dict) or any(type(v) is not str for v in grafo):
        raise ValueError("El grafo debe ser un diccionario con nodos de texto")
    for vecinos in grafo.values():
        if not isinstance(vecinos, dict):
            raise ValueError("Los vecinos deben ser un diccionario")
        for vecino, peso in vecinos.items():
            if vecino not in grafo:
                raise ValueError("Todo vecino debe existir como nodo")
            entero(peso, "peso")


def dijkstra(grafo, origen):
    """Devuelve distancia y predecesor para TODOS los nodos desde origen."""
    validar_grafo(grafo)
    if origen not in grafo:
        raise ValueError("Origen inexistente")
    distancia = {nodo: float("inf") for nodo in grafo}
    anterior = {}
    distancia[origen] = 0
    pendientes = [(0, origen)]
    while pendientes:
        costo, actual = heapq.heappop(pendientes)
        if costo != distancia[actual]:
            continue  # Esta entrada quedó vieja después de una mejora.
        for vecino, peso in grafo[actual].items():
            nuevo_costo = costo + peso
            if nuevo_costo < distancia[vecino]:
                distancia[vecino] = nuevo_costo
                anterior[vecino] = actual
                heapq.heappush(pendientes, (nuevo_costo, vecino))
    return distancia, anterior


def ruta_minima(grafo, origen, destino, bloqueados=()):
    validar_grafo(grafo)
    if origen not in grafo or destino not in grafo:
        raise ValueError("Origen o destino inexistente")
    bloqueados = set(bloqueados)
    if not bloqueados <= grafo.keys():
        raise ValueError("Zona bloqueada inexistente")
    if origen in bloqueados or destino in bloqueados:
        raise ValueError("Origen o destino bloqueado")
    activos = {u: {v: p for v, p in vecinos.items() if v not in bloqueados}
               for u, vecinos in grafo.items() if u not in bloqueados}
    distancia, anterior = dijkstra(activos, origen)
    if distancia[destino] == float("inf"):
        return [], float("inf")
    ruta = [destino]
    while ruta[-1] != origen:
        ruta.append(anterior[ruta[-1]])
    ruta.reverse()
    return ruta, distancia[destino]


def fecha(texto):
    """DD/MM/AAAA estricto. Se ordenan fechas reales, nunca sus textos."""
    try:
        valor = datetime.strptime(texto, "%d/%m/%Y").date()
        if valor.strftime("%d/%m/%Y") != texto:
            raise ValueError()
        return valor
    except (ValueError, TypeError):
        raise ValueError("Fecha inválida: use DD/MM/AAAA") from None


def fefo(lotes, cantidad_pedida, hoy):
    """Plan por SKU. Lote: (código, vencimiento DD/MM/AAAA, cantidad libre).

    Vence hoy: aún elegible. Si falta stock se devuelve un diagnóstico parcial,
    pero NO se confirma ninguna reserva ni se cambia el inventario.
    """
    entero(cantidad_pedida, "cantidad_pedida")
    hoy = fecha(hoy)
    candidatos = []
    codigos = set()
    for lote in lotes:
        if not isinstance(lote, (list, tuple)) or len(lote) != 3:
            raise ValueError("Cada lote necesita código, vencimiento y cantidad")
        codigo, vencimiento, disponible = lote
        if type(codigo) is not str or not codigo or codigo in codigos:
            raise ValueError("Código vacío o repetido")
        codigos.add(codigo)
        entero(disponible, "disponible")
        vencimiento = fecha(vencimiento)
        if vencimiento >= hoy and disponible > 0:
            candidatos.append((vencimiento, codigo, disponible))
    candidatos.sort()  # Fecha primero; código como desempate.
    pendiente = cantidad_pedida
    plan = []
    for vencimiento, codigo, disponible in candidatos:
        if pendiente == 0:
            break
        tomar = min(pendiente, disponible)
        plan.append((codigo, tomar))
        pendiente -= tomar
    return {"completo": pendiente == 0, "plan": plan, "faltante": pendiente}


def reposicion(disponible, en_orden, reservado, minimo, objetivo):
    """'disponible' es existencia física utilizable ANTES de restar reservas.

    en_orden incluye solo unidades pendientes de órdenes abiertas. Esta función
    calcula una sugerencia; no crea ni confirma órdenes de compra.
    """
    for nombre, valor in (("disponible", disponible), ("en_orden", en_orden),
                          ("reservado", reservado), ("minimo", minimo),
                          ("objetivo", objetivo)):
        entero(valor, nombre)
    if objetivo < minimo:
        raise ValueError("El objetivo no puede ser menor que el mínimo")
    posicion = disponible + en_orden - reservado
    sugerencia = max(0, objetivo - posicion) if posicion <= minimo else 0
    return posicion, sugerencia
