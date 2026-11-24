import unittest
from codigo.correos import *
from codigo.demo import resultados

class Correos(unittest.TestCase):
    def test_p1_normal_y_no_alcanzable(self):
        g={'A':{'B':1},'B':{},'C':{}}
        self.assertTrue(alcanzable(g,'A','B'));self.assertFalse(alcanzable(g,'A','C'))
    def test_p1_limite(self):
        self.assertTrue(alcanzable({'A':{}},'A','A'))
    def test_p1_invalido(self):
        with self.assertRaises(ValueError): alcanzable({'A':{}},'X','A')
    def test_p3_normal(self):
        self.assertEqual(resultados()['p3'][0],10)
    def test_p3_limite(self):
        self.assertEqual(flujo_maximo({'A':{},'B':{}},'A','B'),(0,[]))
    def test_p3_invalido(self):
        with self.assertRaises(ValueError): flujo_maximo({'A':{'B':-1},'B':{}},'A','B')
    def test_n1_normal(self):
        self.assertTrue(resultados()['n1']['verificado'])
    def test_n1_limite_y_no(self):
        self.assertEqual(buscar_isomorfismo([],[]),())
        self.assertIsNone(buscar_isomorfismo([[0]],[[0,1],[1,0]]))
    def test_n1_certificado_invalido(self):
        self.assertFalse(verificar_isomorfismo([[0,1],[1,0]],[[0,1],[1,0]],[0,0]))
    def test_n1_entrada_invalida(self):
        with self.assertRaises(ValueError): buscar_isomorfismo([[0,1]],[[0]])
    def test_n2_normal(self):
        self.assertEqual(buscar_factor(91,10),7);self.assertTrue(verificar_factor(91,10,7))
    def test_n2_limites(self):
        self.assertIsNone(buscar_factor(13,1));self.assertIsNone(buscar_factor(13,12))
        self.assertEqual(buscar_factor(13,13),13)
    def test_n2_certificado_invalido(self):
        for d in [0,1,6,13,True,None]: self.assertFalse(verificar_factor(91,10,d))
    def test_n2_entrada_invalida(self):
        with self.assertRaises(ValueError): buscar_factor(-91,10)
    def test_n3_normal(self):
        self.assertEqual(buscar_exponente(23,5,8,10),6)
        self.assertTrue(verificar_exponente(23,5,8,10,6))
    def test_n3_limites(self):
        self.assertEqual(buscar_exponente(23,5,1,0),0)
        self.assertIsNone(buscar_exponente(23,5,8,5))
    def test_n3_certificado_invalido(self):
        self.assertFalse(verificar_exponente(23,5,8,10,11))
        self.assertFalse(verificar_exponente(23,5,8,10,5))
    def test_n3_entrada_invalida(self):
        with self.assertRaises(ValueError): buscar_exponente(1,5,8,10)
    def test_n4_normal(self):
        self.assertTrue(resultados()['n4']['verificado'])
    def test_n4_limite(self):
        self.assertIsNone(buscar_automorfismo([[0]]))
    def test_n4_identidad_rechazada(self):
        self.assertFalse(verificar_automorfismo([[0,1],[1,0]],[0,1]))
    def test_n4_entrada_invalida(self):
        with self.assertRaises(ValueError): buscar_automorfismo([[2]])
    def test_c1_normal(self):
        self.assertEqual(buscar_sat([[1,-2],[2,3]],3),(False,False,True))
    def test_c1_limite_y_no(self):
        self.assertEqual(buscar_sat([],0),());self.assertIsNone(buscar_sat([[1],[-1]],1))
    def test_c1_certificado_invalido(self):
        self.assertFalse(verificar_sat([[1]],1,[False]))
        self.assertFalse(verificar_sat([[1]],1,[1]))
    def test_c1_entrada_invalida(self):
        with self.assertRaises(ValueError): buscar_sat([[0]],1)
    def test_c2_normal(self):
        self.assertEqual(buscar_tsp([[0,4,8],[4,0,3],[8,3,0]],20),((0,1,2,0),15))
    def test_c2_limite_y_no(self):
        self.assertEqual(buscar_tsp([[0]],0),((0,0),0))
        self.assertIsNone(buscar_tsp([[0,4,8],[4,0,3],[8,3,0]],14))
    def test_c2_certificado_invalido(self):
        self.assertFalse(verificar_tsp([[0,1],[1,0]],5,[0,0,0]))
        self.assertFalse(verificar_tsp([[0,1],[1,0]],5,[0,1]))
    def test_c2_entrada_invalida(self):
        with self.assertRaises(ValueError): buscar_tsp([[0,-1],[-1,0]],20)
    def test_c3_normal(self):
        self.assertEqual(resultados()['c3']['certificado'],['B'])
    def test_c3_limite_y_no(self):
        self.assertEqual(buscar_cobertura({'A':{}},0),[])
        self.assertIsNone(buscar_cobertura({'A':{'B':1},'B':{'A':1}},0))
    def test_c3_certificado_invalido(self):
        g={'A':{'B':1},'B':{'A':1,'C':1},'C':{'B':1}}
        for s in [['A'],['X'],['B','B']]: self.assertFalse(verificar_cobertura(g,1,s))
    def test_c3_entrada_invalida(self):
        with self.assertRaises(ValueError): buscar_cobertura({'A':{'B':1},'B':{}},1)
    def test_demo_todos_certificados(self):
        r=resultados()
        for c in ['n1','n2','n3','n4','c1','c2','c3']:
            self.assertTrue(r[c]['verificado'],c)
