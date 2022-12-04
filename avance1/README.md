# Avance 1

<p align = "center">

# <p align = "center"> Maestría en Ciencia de Datos del ITAM :computer:
    
# <p align = "center"> Métodos Numéricos y Optimización (Otoño 2022)    
    
# <p align = "center"> Proyecto Final: Superficies de Delaunay. Una perspectiva desde el cálculo de variaciones.
  
# <p align = "center"> Equipo 2

## Integrantes 👨‍🔬 👨‍🔬 👩‍🔬 👨‍🔬

|     ***Contributors***           |             ***Usuario de Github***                  |  ***Roles***  |                               
|:--------------------------------:|:----------------------------------------------------:|:----------------------:|
|        David Damián Arbeu        |     [David-Damián](https://github.com/David-Damian)  |       Grupo de programación   | 
| Juan Francisco Palmeros Barradas | [JuanPalms](https://github.com/JuanPalms)            |       Grupo de programación   | 
|       Valeria Roberts Trujillo   |  [ValeriaRoberts](https://github.com/ValeriaRoberts) |       Project manager   | 
|  José Alberto Mandujano Montes   | [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes) |       Grupo de revisión  |

## :rocket: ```Título del proyecto``` Superficies de Delaunay

## Trabajo: [Reporte Superficies de Delaunay](https://colab.research.google.com/drive/1XA9aNb8SYYdMDgU99fKH2e19lZBY3FJR?usp=sharing)

### Resúmen

Resolvimos el *milestone* (...) relacionado con los *issues* (...) para la tarea (...)

Revisamos (...) con diferentes parámetros y generamos el reporte (...)


### Individual

[David-Damián](https://github.com/David-Damian): 

Leí la siguiente [referencia](http://docs.nvidia.com/cuda/cuda-c-programming-guide/#axzz4cvQxAHMZ) para revisar implementaciones de la multiplicación de matrices en una GPU. Debo revisar las asignaciones de los índices que se están realizando pues no queda claro el uso de las variables `blockDim` y `blockIdx`, para ello estoy leyendo la sección 3.3 del [libro](http://www.hds.bme.hu/~fhegedus/C++/programming_massively_parallel_processors.pdf).

Implementé la siguiente [funcion_imprime_hello_world_cuda.cu](src/funcion_imprime_hello_world_cuda.cu) en CUDA-C para realizar un hello world.

[JuanPalms](https://github.com/JuanPalms):

Implementé el *testing* para este primer avance en [test_funcion_imprime_hello_world_cuda.cu](src/test/test_funcion_imprime_hello_world_cuda.cu)

### Project manager

Se crearon 5 Issues:
* ***1 Tareas iniciales*** asignado a [David-Damián](https://github.com/David-Damian) y [ValeriaRoberts](https://github.com/ValeriaRoberts)
* ***2 Definición del problema*** asignado a [David-Damián](https://github.com/David-Damian)
* ***3 Programación del método Runge Kutta*** asignado a [David-Damián](https://github.com/David-Damian) y [JuanPalms](https://github.com/JuanPalms)
* ***4 Testing*** asignado a [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes)
* ***5 Reporte*** asignado a [ValeriaRoberts](https://github.com/ValeriaRoberts)
* ***6 Reporte Avance 2*** asignado a [ValeriaRoberts](https://github.com/ValeriaRoberts)

Y se crearon 2 *milestone*
* Avance 1
* Avance 2

Resolvimos el *milestone* Avance 1 relacionado con los *issues* (1-5) para contar con el 

Además se adelanto el Reporte final en un 50%. Donde se incluyeron las siguientes secciones:
* Resumen
* Introducción al cálculo de variaciones
    * ¿Qué estudia el cálculo de variaciones?
* Problemas clásicos de optimización
    * Problema de la braquistocrona
    * Problema sobre geodésicas
* Formulación y solución matemática del problema de optimización
    * Solución matemática del problema
        * Solución vía métodos numéricos
            * Método de Runge Kutta de orden 4

### Grupo de programación [David-Damián](https://github.com/David-Damian) y [JuanPalms](https://github.com/JuanPalms)

Se programo el método de Runge-kutta, el cual sirve para aproximar la solución del problema de valor inicial del tipo

$$y'=f(t,y)   t\in[a,b] y (a)=\alpha$$

Para comprobar la efectividad del método se utilizó el problema siguiente:

$$ y'=y\quad y(0)=1 $$ 

ya que ese problema tiene la solución analítica $y(t)=\exp(t)$.
Los resultados muestran que la solución numérica es muy similar a la analítica, calculando el error relativo. Por lo que se puede concluir que el método funciona correctamente.

Además se graficó el sólido de revolución enfocado al problema específico que buscamos resolver. Este se encuentra explicado con máyor detalle aquí.

### Grupo de revisión [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes)

Revisamos (...) con diferentes parámetros y generamos el reporte (...)


---

## Tarea (o *milestone* o trabajo) que continúa

Determinamos que nos tomará dos días revisar los índices de las referencias que mencionó Erick y revisaremos la implementación de Erica para que la [funcion_imprime_hello_world_cuda.cu](src/funcion_imprime_hello_world_cuda.cu) imprima un `hello_world` por cada bloque de threads.

Falta completar las siguientes secciones en el Reporte:
* Antecedentes históricos del problema de optimización
* Resultados
    * Interpretación de los resultados
* Conclusión
* Bibliografía
