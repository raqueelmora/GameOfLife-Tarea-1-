## Descripción del Repositorio

En este repositorio encontrarás dos archivos principales:

1. Juego de la Vida

- Archivo: game_of_life.py
- Descripción: Este archivo implementa el Juego de la Vida de Conway. Se ejecuta el juego y se crea una visualización gráfica de la evolución de las celdas.
- Cómo Ejecutar: Para ejecutar el código, abre la terminal y usa el siguiente comando: python game_of_life.py


2. Rendimiento

- Archivo: rendimiento.py
- Descripción: Este archivo realiza pruebas de rendimiento variando el tamaño de la grilla. Genera una visualización log-log que muestra una gráfica del tiempo promedio por iteración en función del tamaño de entrada (número de celdas).
- Cómo Ejecutar: Para ejecutar el código de pruebas de rendimiento, abre la terminal y usa el siguiente comando: python rendimiento.py

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas antes de ejecutar los archivos:

numpy
matplotlib

Puedes instalarlas usando pip:

pip install numpy matplotlib

## Notas
Asegúrate de estar en el directorio correcto donde se encuentran los archivos antes de ejecutar los comandos.
Las visualizaciones se generarán en ventanas emergentes, asegúrate de que tu entorno de desarrollo soporte gráficos.

## Ejecución

### Simulación y Visualización
 Aquí se puede visualizar el Game of Life con un tamaño fijo (50x50) y observar la dinámica del autómata.

https://ulead-my.sharepoint.com/:v:/g/personal/raquel_mora_ulead_ac_cr/EXO9Gl0W06FAs-E-xwUtiMwBcNmyQwofhGzCcCjw6xdXkQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=LrR93l

(Usar Link para ver Visualización)

## Análisis de rendimiento
Se probó la simulación con diferentes tamaños (32, 64, 128, 256, 512, 1024) y 10 iteraciones cada una.

Estos fueron nuestros resultados:

Tamaño: 32x32, Tiempo promedio por iteración: 0.001953 segundos
Tamaño: 64x64, Tiempo promedio por iteración: 0.007990 segundos
Tamaño: 128x128, Tiempo promedio por iteración: 0.031868 segundos
Tamaño: 256x256, Tiempo promedio por iteración: 0.127511 segundos
Tamaño: 512x512, Tiempo promedio por iteración: 0.541824 segundos
Tamaño: 1024x1024, Tiempo promedio por iteración: 2.215804 segundos

Gráfica del rendimiento:
<img width="931" alt="Screenshot 2025-06-18 at 5 03 22 PM" src="https://github.com/user-attachments/assets/a6745d2f-557f-41ec-adf6-06db8bedddac" />

## Análisis Resultados

