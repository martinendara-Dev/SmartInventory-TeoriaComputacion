# Validación realizada

- Python: `python -m unittest discover -s tests -v`. Resultado: 61 métodos de prueba correctos. Incluyen 19 subcasos de cadenas de autómatas. Salida en `pruebas.txt`.
- Demostración: `python -m codigo.demo`. Salida observada en `demo.json`.
- JFLAP: se descargó el JAR oficial 7.1 y se decodificaron los tres `.jff` con `file.XMLCodec`. Cada secuencia se ejecutó mediante `automata.fsa.FSAStepByStateSimulator.simulateInput`. Resultado: 19 cadenas coinciden con lo esperado. Salida en `jflap.txt`.

La validación JFLAP se hizo con su motor real en modo sin interfaz gráfica. No se presentan capturas de pantalla ni se afirma haber hecho clic en Multiple Run. Las instrucciones del README permiten repetir los casos en la interfaz del programa. `ProbarJFLAP.java` permite repetir la ejecución del motor.

Los resultados describen datos pequeños y deterministas. No son una medición del rendimiento en una planta real. Las cotas Big-O se justifican por el algoritmo, no por los milisegundos que muestran las pruebas.
