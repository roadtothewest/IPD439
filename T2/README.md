# Tarea 2: Sistemas en Tiempo Real con FreeRTOS 
**Autor:** Vicente Ramón Andrade Ercilla

Este repositorio contiene los proyectos correspondientes a cada pregunta de la tarea 2. También contiene los scripts Python requeridos.

El directorio se divide funcionalmente según las dos preguntas de la evaluación:

* **`T2IPD439/`**: Proyecto correspondiente a la **Pregunta 1**. Contiene la implementación de tareas periódicas, manejo de prioridades y el análisis de starvation inducido por cargas computacionales de complejidad algorítmica $O(n)$.
* **`T2_2IPD439/`**: Proyecto correspondiente a la **Pregunta 2**. Contiene la implementación de los Subsistemas A (Procesamiento UART y colas) y B (Adquisición ADC periódica y actuación GPIO one-hot).
* **`Scripts/`**: Directorio con las herramientas en Python empleadas para la validación y análisis estadístico.

## Mapeo de Scripts de Python

Cada archivo `.py` fue diseñado para interactuar con un proyecto específico y procesar los datos resultantes:

### Para el Proyecto 1 (`T2IPD439`):

* `analisis_rtos.py`: Identifica las transiciones lógicas en la data cruda (`digital.csv`) y calcula el periodo promedio y la desviación estándar de la temporización original.

* `resultados.py`: Herramienta que itera sobre múltiples conjuntos de datos (`50000.csv`, `100000.csv`, etc.) para calcular numéricamente el impacto de las cargas computacionales en las métricas de tendencia y *jitter*.

* `graficos.py`: Emplea la librería `matplotlib` para procesar los mismos archivos de carga estructurados, consolidando los cálculos en *DataFrames* y exportando de forma automática los diagramas de barras requeridos en el informe.

### Para el Proyecto 2 (`T2_2IPD439`): 

* `tarea2_2IPD439.py`: Cliente UART para pruebas de estrés. Se encarga de generar dinámicamente un arreglo de 100 valores aleatorios de punto flotante, empaquetarlos estructuralmente (`<100f`) junto a la cabecera de control (`0xAA 0xBB 0xCC 0xDD`) y despacharlos al microcontrolador. Posteriormente, captura la cadena formateada de retorno y valida empíricamente si la desviación estándar y el promedio calculados por la MCU coinciden con la teoría.
