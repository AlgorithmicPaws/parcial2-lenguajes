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
antlr4 -Dlanguage=Python3 NombreArchivo.g4 -visitor -o
python3 Main.py ejemplos.txt
```
IMPORTANTE:

Reemplace `NombreArchivo.g4` con el nombre del archivo de gramática específico que desea ejecutar, y `ejemplos.txt` con el nombre del archivo de entrada que desea utilizar, o déjelo en blanco para abrir la entrada por consola.

* Para el Punto #1. el archivo .g4 se llama: `ComplexLanguage.g4`

Recomendaciones Punto #1: El programa maneja los numeros imaginarios como: los numeros enteros seguidos de un operador de suma o resta seguido de un numero entero acompañado de una 'i'. O directamente como un numero entero seguido de una 'i'. Se pueden manejar operaciones con imaginarios de suma, resta, multipliación y división, al igual que expresiones con parentesis.

* Para el Punto #2. el archivo .g4 se llama:

Recomendaciones Punto #2:

* Para el punto #3. el archivo .g4 se llama:

Recomendaciones Punto #2:

Todos las carpetas tienen llamado el archivo principal que ejecuta todo como `Main.py`

