# LOGISTPULSE · Deber 2 de Teoría de la Computación

USFQ. Integrantes: **Martin Endara, Isaac Espinoza, Sol Segovia y Emily Cadena**.

Este proyecto explica y prueba los procesos de pedidos, reservas y compras. Incluye los diez correos del simulador, sus algoritmos y verificadores. La implementación es didáctica, sin interfaz ni base de datos. Las búsquedas exhaustivas están pensadas para datos pequeños.

## 1. Abrir el proyecto

Descargar el ZIP del repositorio y extraerlo, o usar:

```bash
git clone https://github.com/martinendara-Dev/SmartInventory-TeoriaComputacion.git
cd SmartInventory-TeoriaComputacion
```

Abrir esa carpeta en VS Code. En Terminal > Nueva terminal, comprobar que se está en la carpeta que contiene este README, `codigo` y `tests`.

## 2. Ejecutar los ejemplos

Requisito: **Python 3.10 o superior**. No hay que instalar paquetes.

```bash
python --version
python -m codigo.demo
```

En Windows, si `python` no funciona, sustituirlo por `py`:

```powershell
py -m codigo.demo
```

La demo imprime los resultados en JSON para que se distingan las entradas de salida por caso. Las funciones de procesamiento no leen archivos ni imprimen. Solo `codigo/demo.py` carga el grafo y presenta resultados. No ejecutar `codigo/correos.py` directamente: es un módulo para importar.

Resultados principales:

| Caso | Resultado |
|---|---|
| AMR | R → B → A → E → D, 11 metros |
| FEFO, 8 unidades | A01: 3, A02: 4, B01: 1 |
| Reposición | Posición 23, sugerencia 27 |
| Reposición después de abrir la compra | Posición 50, sugerencia 0 |
| p1 | Norte es alcanzable |
| p2 | Quito → Latacunga → Guayaquil, costo 8 |
| p3 | 10 camiones por día |
| n1 | Permutación (1, 0, 2) |
| n2 | Divisor 7 |
| n3 | Exponente 6 |
| n4 | Permutación no identidad (0, 2, 1) |
| c1 | (False, False, True) |
| c2 | (0, 1, 2, 0), costo 15 ≤ 20 |
| c3 | Elegir B cubre ambos corredores |

Todos los certificados de n1–n4 y c1–c3 se verifican aparte de su búsqueda. En JSON, las tuplas se muestran como listas y True como `true`.

## 3. Ejecutar las pruebas

```bash
python -m unittest discover -s tests -v
```

En Windows: `py -m unittest discover -s tests -v`.

Resultado esperado: **Ran 61 tests ... OK**. Los subcasos de autómatas comprueban además 19 cadenas. Un `ok` significa que el resultado coincide con lo esperado. `ValueError` dentro de una prueba de entrada inválida es el comportamiento correcto, no un fallo. Si aparece `FAILED`, leer el nombre y la comparación indicada.

Pruebas normales: ruta mínima, orden FEFO, compra, diez expedientes y certificados. Límites: mismo origen, distancia cero, grafo desconectado, cero demanda, falta de stock, inventario vacío, cota cero, fórmula vacía y un solo centro. Inválidas: pesos negativos, nodos inexistentes, fechas imposibles, códigos repetidos, matrices mal formadas y certificados falsos.

## 4. Probar los autómatas en JFLAP

1. Obtener JFLAP 7.1 desde https://www.jflap.org/jflaptmp/ y disponer de Java.
2. Abrir `modelos/pedido.jff` en JFLAP con File > Open.
3. Seleccionar Input > Multiple Run.
4. Usar Load Inputs y abrir `modelos/pedido_entradas.txt`, o escribir las cadenas sin espacios, una por fila.
5. Pulsar Run Inputs. Comparar Accept/Reject con el informe y `evidencias/jflap.txt`.
6. Repetir con `reserva.jff` y `compra.jff` y sus archivos de entradas.
7. Usar View Trace para explicar el primer evento que manda a Error.

Las letras representan eventos; su significado cambia según el autómata y está en el informe. Los archivos `.jff` contienen todas las transiciones hacia Error. Los diagramas omiten esas flechas para que se puedan leer. Una cadena que queda a mitad de trámite no se acepta como proceso terminado.

También se ejecutaron las 19 secuencias mediante el motor original del JAR oficial, sin interfaz gráfica. Se puede repetir con un JDK 11 o superior, desde esta carpeta:

```bash
java -Djava.awt.headless=true -cp /ruta/JFLAP7.1.jar modelos/ProbarJFLAP.java modelos
```

En Windows, cambiar `/ruta/JFLAP7.1.jar` por la ruta real entre comillas. `ProbarJFLAP.java` es solo un comprobador opcional del motor JFLAP; el proyecto principal sigue siendo Python. El JAR no se redistribuye en el repositorio.

## 5. Leer y presentar

- `documentos/Informe_LOGISTPULSE.pdf`: informe breve de seis páginas, con los tres modelos formales, grafo, pseudocódigos y nota de una página sobre parada.
- `documentos/Fichas_10_correos.pdf`: tabla resumen y diez fichas con entradas, certificados, reducciones, costos y resultados.
- `documentos/Presentacion_LOGISTPULSE.pptx`: diez diapositivas editables, con notas para hablar.
- `documentos/Guion_exposicion.pdf`: reparto sugerido y guion de nueve minutos.
- `documentos/Nota_parada.pdf`: la última página del informe, también por separado.
- `diagramas/`: PNG para visualizar, SVG y DOT para editar los diagramas.
- `datos/`: grafo, modelos, guion y correos originales.
- `evidencias/`: salidas reales de Python y JFLAP.
- `gestion/`: backlog, plan de tres sprints, contribuciones y release.

## 6. Decisiones que hay que entender

1. La planta tiene dos rutas óptimas de 11 m. La de la consigna pasa por P; Dijkstra conserva la primera encontrada, que pasa directamente de A a E.
2. FEFO recibe lotes de un SKU y cantidades libres; reposición recibe existencia física antes de restar reservas. Fechas: DD/MM/AAAA, convertidas a fechas antes de ordenar.
3. El plan FEFO no modifica stock. Si falta cantidad, no se confirma la reserva parcial.
4. La reposición calcula una sugerencia. Evitar compras duplicadas en un sistema real requiere actualizar la orden y su pendiente de forma atómica. Aquí se prueba el cálculo antes y después de abrir la orden.
5. En n3 se supone p primo, como indica el expediente. Se validan rangos, no se certifica primalidad.
6. El cuerpo del correo c3 pide Vertex Cover: cubrir **aristas**, no cubrir zonas vecinas.
7. El SAT de dos literales del expediente es fácil. La prueba de NP-completitud se refiere a la familia general que admite tres literales.
8. Se documentan commits por bloque de sprint, sin simular semanas ni atribuir a integrantes revisiones que no hicieron.

## 7. Entrega

Subir al curso el enlace al repositorio y el informe PDF. Adjuntar las fichas o el ZIP completo con código, datos, diagramas y JFLAP. La etiqueta `v1.0.0` está preparada en el historial local. La publicación en GitHub la hará Martin siguiendo `SUBIR_A_GITHUB.md`. Antes de exponer, cada integrante debe ejecutar las pruebas y ensayar su parte.
