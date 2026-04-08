# Tarea 2: Sistemas en Tiempo Real con FreeRTOS - IPD439 / ELO320

**Autor:** Vicente Ramón Andrade Ercilla
**Programa:** Ingeniería Civil Electrónica 

Este repositorio contiene la arquitectura de firmware, configuración de hardware y scripts de validación para la implementación de sistemas concurrentes utilizando FreeRTOS sobre un microcontrolador STM32. El repositorio se estructura en dos proyectos principales que dan solución a los requerimientos de temporización estricta y comunicación asíncrona.

## Estructura del Repositorio

El directorio se divide funcionalmente según las dos preguntas de la evaluación:

* **`T2IPD439/`**: Proyecto de STM32CubeIDE correspondiente a la **Pregunta 1**. Contiene la implementación de tareas periódicas, manejo de prioridades y el análisis de inanición (*starvation*) inducido por cargas computacionales de complejidad algorítmica $O(n)$.
* **`T2_2IPD439/`**: Proyecto de STM32CubeIDE correspondiente a la **Pregunta 2**. Contiene la implementación de los Subsistemas A (Procesamiento UART asíncrono y colas) y B (Adquisición ADC periódica y actuación GPIO mutuamente excluyente).
* **`Scripts/`**: Directorio con las herramientas en Python empleadas para la validación de hardware y análisis estadístico.

## Mapeo de Scripts de Python

Cada archivo `.py` fue diseñado para interactuar con un proyecto específico y procesar los datos resultantes:

### Para el Proyecto 1 (`T2IPD439`): Tareas Periódicas y Jitter
Estos scripts procesan las capturas digitales extraídas desde el analizador lógico en formato CSV para determinar la exactitud y precisión del RTOS.

* `analisis_rtos.py`: Script de evaluación base. Identifica las transiciones lógicas en la data cruda (`digital.csv`) y calcula el periodo promedio y la desviación estándar de la temporización original.
* `resultados.py`: Herramienta de procesamiento masivo por terminal. Itera sobre múltiples conjuntos de datos (`50000.csv`, `100000.csv`, etc.) para calcular numéricamente el impacto de las cargas computacionales en las métricas de tendencia y *jitter*.
* `graficos.py`: Automatizador de figuras. Emplea la librería `matplotlib` para procesar los mismos archivos de carga estructurados, consolidando los cálculos en *DataFrames* y exportando de forma automática los diagramas de barras (`tendencia_carga.png` y `varianza_carga.png`) requeridos en el informe.

### Para el Proyecto 2 (`T2_2IPD439`): Subsistemas y Colas
Script destinado a la prueba de concepto del hardware in-the-loop del Subsistema A.

* `tarea2_2IPD439.py`: Cliente UART para pruebas de estrés. Se encarga de generar dinámicamente un arreglo de 100 valores aleatorios de punto flotante, empaquetarlos estructuralmente (`<100f`) junto a la cabecera de control (`0xAA 0xBB 0xCC 0xDD`) y despacharlos al microcontrolador. Posteriormente, captura la cadena formateada de retorno y valida empíricamente si la desviación estándar y el promedio calculados por la MCU coinciden con la teoría.
