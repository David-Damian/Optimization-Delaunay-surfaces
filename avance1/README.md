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

## Trabajo: 

### Resúmen

Resolvimos el *milestone* (...) relacionado con los *issues* (...) para la tarea (...)

Revisamos (...) con diferentes parámetros y generamos el reporte (...)


### Individual

Erick: 

Leí la siguiente [referencia](http://docs.nvidia.com/cuda/cuda-c-programming-guide/#axzz4cvQxAHMZ) para revisar implementaciones de la multiplicación de matrices en una GPU. Debo revisar las asignaciones de los índices que se están realizando pues no queda claro el uso de las variables `blockDim` y `blockIdx`, para ello estoy leyendo la sección 3.3 del [libro](http://www.hds.bme.hu/~fhegedus/C++/programming_massively_parallel_processors.pdf).

Implementé la siguiente [funcion_imprime_hello_world_cuda.cu](src/funcion_imprime_hello_world_cuda.cu) en CUDA-C para realizar un hello world.

Erica:

Implementé el *testing* para este primer avance en [test_funcion_imprime_hello_world_cuda.cu](src/test/test_funcion_imprime_hello_world_cuda.cu)

### Project manager

Se crearon 5 Issues:
* ***1 Tareas iniciales*** asignado a [David-Damián](https://github.com/David-Damian) y [ValeriaRoberts](https://github.com/ValeriaRoberts)
* ***2 Definición del problema*** asignado a [David-Damián](https://github.com/David-Damian)
* ***3 Programación para resolver el problema*** asignado a [David-Damián](https://github.com/David-Damian) y [JuanPalms](https://github.com/JuanPalms)
* ***4 Testing*** asignado a [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes)
* ***5 Reporte*** asignado a [ValeriaRoberts](https://github.com/ValeriaRoberts)
* ***6 Reporte Avance 2*** asignado a [ValeriaRoberts](https://github.com/ValeriaRoberts)

Y se crearon 2 *milestone*
* Avance 1
* Avance 2

Resolvimos el *milestone* Avance 1 relacionado con los *issues* (1-5) para contar con el 

### Grupo de programación

Programamos (...) que puede consultarse (...).

### Grupo de revisión

Revisamos (...) con diferentes parámetros y generamos el reporte (...)


---

## Tarea (o *milestone* o trabajo) que continúa

Determinamos que nos tomará dos días revisar los índices de las referencias que mencionó Erick y revisaremos la implementación de Erica para que la [funcion_imprime_hello_world_cuda.cu](src/funcion_imprime_hello_world_cuda.cu) imprima un `hello_world` por cada bloque de threads.

