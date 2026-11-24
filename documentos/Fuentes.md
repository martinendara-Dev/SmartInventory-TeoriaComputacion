# Fuentes y decisiones de modelado

- Consigna proporcionada: Deber2_Teoria_Computacion_LOGISTPULSE_USFQ.docx, 17/11/2026. Estados y grafo tomados de sus figuras 2 a 5.
- Simulador proporcionado: Simulador_LOGISTPULSE_P_NP_NP-completo (2).html. Se conservaron sus diez expedientes y cuerpos de correo en datos/correos_originales.json.
- JFLAP, tutorial oficial de autómatas y Multiple Run: https://jflap.org/csed/jflap/tutorial/fa/createfa/fa.html
- JFLAP 7.1, motor oficial utilizado para las 19 secuencias: https://www.jflap.org/jflaptmp/july27-18/JFLAP7.1.jar
- Kevin Wayne, Princeton, Polynomial-Time Reductions, diapositiva 18: reducción de Ciclo Hamiltoniano a TSP. https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pearson/08PolynomialTimeReductions.pdf
- OpenDSA, Virginia Tech, Independent Set to Vertex Cover: https://opendsa.cs.vt.edu/OpenDSA/Books/CS4104/html/independentSet_to_vertexCover.html
- Sipser, Introduction to the Theory of Computation. Referencia propuesta por la consigna para parada, P y NP.

## Precisiones que afectan la respuesta

1. c3: el cuerpo del correo y su código piden cubrir cada arista (Vertex Cover). La descripción breve que habla de cubrir una zona propia o vecina corresponde a otro problema. Las fichas siguen el cuerpo operativo.
2. c2 exige regresar al inicio, como dice el correo y hace el código del simulador.
3. c1 admite cláusulas de hasta tres literales; el pequeño expediente de dos literales no demuestra por sí solo dureza.
4. Las etiquetas B/NP indican solo pertenencia demostrada, no exclusión de P ni NP-completitud.
5. En reposición, disponible es existencia utilizable antes de restar reservas; en FEFO es cantidad ya libre. No se descuenta dos veces.
6. Los diagramas omiten las flechas hacia Error para ser legibles. Los .jff tienen la función de transición completa.
