import copy
import json
from pathlib import Path
import unittest
from codigo.logistica import dijkstra, ruta_minima, fefo, reposicion

class Rutas(unittest.TestCase):
    def setUp(self):
        self.g = {'A': {'B': 8, 'C': 1}, 'B': {'D': 1}, 'C': {'B': 1}, 'D': {}, 'Z': {}}

    def test_normal_mejora_distancia(self):
        self.assertEqual(ruta_minima(self.g, 'A', 'D'), (['A','C','B','D'], 3))

    def test_limite_mismo_origen(self):
        self.assertEqual(ruta_minima(self.g, 'A', 'A'), (['A'], 0))

    def test_limite_sin_camino(self):
        self.assertEqual(ruta_minima(self.g, 'A', 'Z'), ([], float('inf')))

    def test_limite_peso_cero(self):
        self.assertEqual(ruta_minima({'A': {'B': 0}, 'B': {'A': 0}}, 'A', 'B')[1], 0)

    def test_bloqueo_obliga_desvio(self):
        self.assertEqual(ruta_minima(self.g, 'A', 'D', ['C'])[1], 9)

    def test_invalido_peso_negativo(self):
        with self.assertRaises(ValueError): dijkstra({'A': {'B': -1}, 'B': {}}, 'A')

    def test_invalido_nodo(self):
        with self.assertRaises(ValueError): ruta_minima(self.g, 'X', 'D')

    def test_invalido_vecino_no_declarado(self):
        with self.assertRaises(ValueError): dijkstra({'A': {'B': 1}}, 'A')

    def test_invalido_destino_bloqueado(self):
        with self.assertRaises(ValueError): ruta_minima(self.g, 'A', 'D', ['D'])

    def test_planta_de_consigna(self):
        p = Path(__file__).resolve().parents[1] / 'datos/planta.json'
        g = json.loads(p.read_text())['grafo']
        self.assertEqual(ruta_minima(g, 'R', 'D'), (['R','B','A','E','D'], 11))
        alternativa = ['R','B','A','P','E','D']
        self.assertEqual(sum(g[u][v] for u,v in zip(alternativa,alternativa[1:])),11)

class Inventario(unittest.TestCase):
    def setUp(self):
        self.lotes = [('B','30/11/2026',4), ('A','30/11/2026',3), ('C','01/12/2026',8), ('V','23/11/2026',9)]

    def test_fefo_desempate_y_no_mutacion(self):
        original = copy.deepcopy(self.lotes)
        self.assertEqual(fefo(self.lotes, 8, '24/11/2026'),
                         {'completo': True, 'plan': [('A',3),('B',4),('C',1)], 'faltante': 0})
        self.assertEqual(self.lotes, original)

    def test_fefo_limite_demanda_cero(self):
        self.assertEqual(fefo([],0,'24/11/2026')['plan'], [])

    def test_fefo_limite_vacio(self):
        self.assertEqual(fefo([],2,'24/11/2026')['faltante'], 2)

    def test_fefo_insuficiente_no_confirma(self):
        r = fefo(self.lotes,20,'24/11/2026')
        self.assertFalse(r['completo']); self.assertEqual(r['faltante'],5)

    def test_fefo_vencimiento_hoy(self):
        self.assertTrue(fefo([('A','24/11/2026',1)],1,'24/11/2026')['completo'])

    def test_fefo_fecha_real_no_orden_lexico(self):
        self.assertEqual(fefo([('A','01/12/2026',1),('B','30/11/2026',1)],1,'24/11/2026')['plan'], [('B',1)])

    def test_fefo_invalido_fecha(self):
        with self.assertRaises(ValueError): fefo([('A','31/11/2026',1)],1,'24/11/2026')

    def test_fefo_invalido_negativo(self):
        with self.assertRaises(ValueError): fefo(self.lotes,-1,'24/11/2026')

    def test_fefo_invalido_codigo_duplicado(self):
        with self.assertRaises(ValueError): fefo([('A','30/11/2026',1)]*2,1,'24/11/2026')

    def test_reposicion_normal(self):
        self.assertEqual(reposicion(18,10,5,30,50), (23,27))

    def test_reposicion_limite_igual_minimo(self):
        self.assertEqual(reposicion(30,0,0,30,50), (30,20))

    def test_reposicion_limite_posicion_negativa(self):
        self.assertEqual(reposicion(0,0,5,10,20), (-5,25))

    def test_reposicion_orden_abierta_evitar_duplicar(self):
        self.assertEqual(reposicion(18,37,5,30,50), (50,0))

    def test_reposicion_invalido_objetivo(self):
        with self.assertRaises(ValueError): reposicion(10,0,0,30,20)

    def test_reposicion_invalido_tipo(self):
        with self.assertRaises(ValueError): reposicion(True,0,0,30,50)
