# Plan de tres sprints y registro de revisión

Equipo: Martin Endara, Isaac Espinoza, Sol Segovia y Emily Cadena.

Los entregables técnicos se prepararon en una sesión y se separan en tres bloques versionados. Esto **no equivale a tres semanas de reuniones realizadas**. El calendario siguiente es un plan relativo a la fecha de inicio que acuerde el equipo. Los responsables son una propuesta de distribución, no una afirmación de autoría pasada.

| Sprint | Semana | Responsable propuesto | Revisor propuesto | Trabajo | Criterio de aceptación |
|---|---|---|---|---|---|
| 1 | 1 | Martin | Isaac | Autómatas y grafo | Tres DFA con Q, Σ, q₀, F, δ; 2 válidas y 2 inválidas por modelo; planta con pesos |
| 2 | 2 | Isaac y Sol | Emily | Dijkstra, FEFO, reposición y pruebas | Ruta válida, desempate FEFO, cantidades correctas, casos límite e inválidos |
| 3 | 3 | Emily | Martin y Sol | Diez fichas, reducciones, parada, presentación y release | Distribución 3/4/3 justificada, certificados separados, exposición de 8–10 min |

## Revisión técnica disponible

- Sprint 1: tres archivos .jff completos. El motor oficial JFLAP acepta y rechaza correctamente las 19 cadenas de `modelos/pruebas.tsv`.
- Sprint 2: 61 pruebas de Python. Se detectó un empate en la planta y se documentaron las dos rutas de costo 11, manteniendo el algoritmo de mejora estricta.
- Sprint 3: diez expedientes con resultados observados, siete verificadores, informe, fichas y guion. Los documentos explican las diferencias entre 2-CNF y 3-CNF y entre Vertex Cover y Dominating Set.

Estas son verificaciones técnicas automatizadas y revisión del material, **no actas de revisión por pares**.

## Registro que debe completar el equipo durante la cursada

Para cada sprint, añadir aquí su fecha real, asistentes, responsable de revisión y cambios acordados. Después registrar una retrospectiva breve:

| Sprint | Fecha real de revisión | Quién revisó | Qué funcionó | Qué se ajustará |
|---|---|---|---|---|
| 1 | Pendiente de reunión | Pendiente | Pendiente | Pendiente |
| 2 | Pendiente de reunión | Pendiente | Pendiente | Pendiente |
| 3 | Pendiente de reunión | Pendiente | Pendiente | Pendiente |

## Preguntas para la retrospectiva

¿Cada integrante pudo explicar las variables sin leer el código? ¿Las pruebas detectaron un supuesto incorrecto? ¿El tiempo de exposición fue menor a diez minutos? Registrar las respuestas reales y los cambios, sin reconstruir reuniones que no ocurrieron.
