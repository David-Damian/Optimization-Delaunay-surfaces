# Avance 2

<p align = "center">

# <p align = "center"> Maestría en Ciencia de Datos del ITAM :computer:
    
# <p align = "center"> Métodos Numéricos y Optimización (Otoño 2022)    
    
# <p align = "center"> Proyecto Final: Superficies de Delaunay. Una perspectiva desde el cálculo de variaciones.
  
# <p align = "center"> Equipo 1

## Integrantes 👨‍🔬 👨‍🔬 👩‍🔬 👨‍🔬

|     ***Contributors***           |             ***Usuario de Github***                  |  ***Roles***  |                               
|:--------------------------------:|:----------------------------------------------------:|:----------------------:|
|        David Damián Arbeu        |     [David-Damián](https://github.com/David-Damian)  |       Grupo de programación   | 
| Juan Francisco Palmeros Barradas | [JuanPalms](https://github.com/JuanPalms)            |       Grupo de programación   | 
|       Valeria Roberts Trujillo   |  [ValeriaRoberts](https://github.com/ValeriaRoberts) |       Project manager   | 
|  José Alberto Mandujano Montes   | [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes) |       Grupo de revisión  |

## :rocket: ```Título del proyecto``` Superficies de Delaunay

## 🌐 [Trabajo escrito](https://drive.google.com/file/d/1eFj753-au0vghaDgTBWP7twcqc6HtbRp/view?usp=sharing)

## Trabajo:

### Resúmen

Inicialmente se nos reunimos para que cada quien expusiera una propuesta de proyecto. Trás una votación se decidió continuar con la propuesta [David-Damián](https://github.com/David-Damian), _Superficies de Delaunay_, la cual además se discutió con el profesor Erick para constar con su aprobacion.
    
Posteriormente se creó el repositorio y se continuo con especificaciones iniciales correspondientes a detalles del README y a la estructura inicial del proyecto. Además el project manajer [ValeriaRoberts](https://github.com/ValeriaRoberts) creo una seríe de *issues* relacionados a 2 *milestone*, uno para el primer avance y otro para el segundo avance.
    
Todos los equipos: programación, testing y project manager cumplieron con el *primer milestone* asociado al avance 1, cerrando los *issues* a tiempo.
A continuación se explicará con mayor detalle las especificaciónes de estos *issues*.

### Grupo de programación [David-Damián](https://github.com/David-Damian) y [JuanPalms](https://github.com/JuanPalms)

Se refinó la lógica de programación del método de Runge-Kutta ya que en ocasiones las soluciones de ecuaciones diferenciales  no eran correctas

Así mismo, programamamos la funcion `delunay` que se encuentra en la ruta `/src/utils1.py` de este respositorio. Dicha función nos permitió implementar una especie de *grid search* para encontrar hiperparámetros que nos permitieran generar las superficies de Delaunay.

#### Individual

[David-Damián](https://github.com/David-Damian): 

-

[JuanPalms](https://github.com/JuanPalms):

 - 

### Grupo de revisión [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes)

Cree los archivos del test para ir haciendo pruebas. Para realizar esta tarea se utilizó un dummy test que solo válida 1==1 para hacer las pruebas iniciales que nos servirán al momento de probar los resultados del problema. 
Esto se realizo a través de un pull request el cual no ha sido aceptado ya que aún requiere más pruebas y ajuste de detalles.

### Project manager [ValeriaRoberts](https://github.com/ValeriaRoberts)

Se crearon 5 Issues:
* ***1 Tareas iniciales*** asignado a [David-Damián](https://github.com/David-Damian) y [ValeriaRoberts](https://github.com/ValeriaRoberts)
* ***2 Definición del problema*** asignado a [David-Damián](https://github.com/David-Damian)
* ***3 Programación del método Runge Kutta*** asignado a [David-Damián](https://github.com/David-Damian) y [JuanPalms](https://github.com/JuanPalms)
    * ***3.1 Programación para resolver el problema*** asignado a [David-Damián](https://github.com/David-Damian) y [JuanPalms](https://github.com/JuanPalms)
* ***4 Dummy Testing*** asignado a [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes)
    * ***4. 1 Final Testing*** asignado a [AlbertoMandujanoMontes](https://github.com/AlbertoMandujanoMontes)
* ***5 Reporte*** asignado a [ValeriaRoberts](https://github.com/ValeriaRoberts)
    * ***5.1 Reporte Final*** asignado a [ValeriaRoberts](https://github.com/ValeriaRoberts)

Y se crearon 2 *milestone*
* Avance 1 el cual esta asociado a los issues $i.0$, $i=1,2,...5$
* Avance 2 el cual esta asociado a los issues $i.1$, $i=3,4,5$

Resolvimos el *milestone* Avance 1 relacionado con los *issues* $i.0$, $i=1,2,...5$ para contar con las especificaciónes correspondientes en tiempo y forma.

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

---

## Tarea (o *milestone* o trabajo) que continúa

Determinamos que nos tomará una semana en revisar nuevamente el trabajo detallado que ha realizado cada individuo para hacer correciones y agregar los detalles finales que hacen falta en cada equipo. Una vez que se complete esto se podrá cumplir con el *milestone* relacionado al Avance 2

Equipo de programación:
Dado que funciona correctamente el método de runge kutta de orden cuato. Falta implementarlo a nuestro problema de interés. Estos detalles estan asociado el *issue* 3.1 Programación para resolver el problema

Equipo de testing:
Falta adaptar el código de testing para que sea aplicable a la solución del problema de interés. Estos detalles estan asociado el *issue* 4. 1 Final Testing

Project Manager.
Falta supervisar que se cumplan los últimos tres *issues* asociados al avance dos.
Además, falta completar las siguientes secciones en el Reporte:
* Antecedentes históricos del problema de optimización
* Resultados
    * Interpretación de los resultados
* Conclusión
* Bibliografía
Los detalles que faltan en el reporte estan asociados al *issue* 5.1 Reporte Final
