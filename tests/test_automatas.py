import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]

class Automatas(unittest.TestCase):
    def test_modelos_dfa_totales_y_secuencias(self):
        datos=json.loads((ROOT/'datos/automatas.json').read_text(encoding='utf-8'))
        for nombre,modelo in datos.items():
            xml=ET.parse(ROOT/'modelos'/f'{nombre}.jff').getroot().find('automaton')
            estados=xml.findall('state')
            inicial=next(e.attrib['id'] for e in estados if e.find('initial') is not None)
            finales={e.attrib['id'] for e in estados if e.find('final') is not None}
            delta={}
            for t in xml.findall('transition'):
                clave=(t.findtext('from'),t.findtext('read'))
                self.assertNotIn(clave,delta)
                delta[clave]=t.findtext('to')
            self.assertEqual(len(delta),len(estados)*len(modelo['eventos']))
            for cadena,esperado,_ in modelo['pruebas']:
                with self.subTest(modelo=nombre,cadena=cadena):
                    actual=inicial
                    for simbolo in cadena: actual=delta[(actual,simbolo)]
                    self.assertEqual(actual in finales,esperado)
            self.assertNotIn(inicial,finales)
