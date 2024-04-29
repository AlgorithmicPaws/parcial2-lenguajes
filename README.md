# Parcial 2: Gramáticas

# Lenguajes de Programación y Transducción G02
## Integrantes del Grupo:
- Santiago Castellanos
- Sergio Florez
- Catalina Gutierrez
- Camilo Millan

Este repositorio contiene la implementación de gramáticas para el Parcial 2. Está organizado en tres carpetas, una por cada punto del parcial, y todos los archivos están generados a partir de antlr4 con lenguaje objetivo Python.

Cada carpeta contiene un archivo `ejemplo.txt` que puede utilizarse para probar la gramática. Este archivo puede ser editado para realizar modificaciones. Sin embargo, al ejecutar el programa, se puede especificar otro archivo `.txt` como entrada, o simplemente no adjuntar ninguno para abrir la entrada por consola.

Para ejecutar el programa, asegúrese de tener configurado correctamente el entorno antlr4 con el lenguaje objetivo Python, estar en la carpeta correspondiente al punto y luego ejecute los siguientes comandos:

```bash
antlr4 -Dlanguage=Python3 -visitor NombreArchivo.g4 
python3 Main.py ejemplos.txt   # o ejemplo.txt según corresponda
```
IMPORTANTE:

Reemplace `NombreArchivo.g4` con el nombre del archivo de gramática específico que desea ejecutar, y `ejemplos.txt` con el nombre del archivo de entrada que desea utilizar, o déjelo en blanco para abrir la entrada por consola.

* Para el Punto #1. el archivo .g4 se llama: `ComplexLanguage.g4`

Recomendaciones Punto #1: El programa maneja los numeros imaginarios como: los numeros enteros o decimales seguidos de un operador de suma o resta seguido de un numero entero o decimal acompañado de una 'i'. O directamente como un numero entero o decimal seguido de una 'i'. Se pueden manejar operaciones con imaginarios de suma, resta, multipliación y división, al igual que expresiones con parentesis.

* Para el Punto #2. el archivo .g4 se llama: `PythonFunction.g4`

Recomendaciones Punto #2: Hasta este momento solo recibe iterables (listas, tuplas y sets, que solo contienen numeros) y se puede hacer filtros con condiciones simples como `elementos_iterable == 3`.

* Para el punto #3. el archivo .g4 se llama: `FourierTransform.g4`

Recomendaciones Punto #3: Acepta 8 tipos de funciones para calcular su transformada segun la tabla de pares transformados: 
- Pulso rectangular como `{1, |t| < T | 0, |t|>T` (La magnitud de la amplitud puede ser cualquier numero positivo, igual que con la longitud de pulso, que puede ser un numero, T o T/2)
- Pulso triangular como `{1 - (|t|/T), |t| < T | 0, |t|>T` donde T puede ser un numero o solo T
- Sign(t) como `{1, |t| < 0 | -1, |t|>0` donde los resultados de cada declaracion, tienen que ser 1 y -1, las condiciones tienen que ser con respecto a 0
- U(t) como `{1, |t| < 0 | 0, |t|>0` donde los resultados de cada declaracion, tienen que ser 1 y 0, las condiciones tienen que ser con respecto a 0
- delta de dirac como `dirac( t )`
- coseno como 'cos(w t)' La frecuencia angular w puede ser un entero o w
- seno como 'sin(w t)' La frecuencia angular w puede ser un entero o w
- Sumatoria como `SUM( dirac( t - k*T)` donde T puede ser un entero o T 

Todos las carpetas tienen llamado el archivo principal que ejecuta todo como `Main.py`

