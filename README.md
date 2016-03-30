# fakeSched

Este software ejemplifica algunos conceptos de administración de
procesos en un sistema operativo. Se desarrolla como parte del curso
"Sistemas Operativos" impartido por el Dr. Yoel Ledo en el
programa de [Maestría en Ciencias de la Computación de la Fundación
Arturo Rosenblueth](http://www.rosenblueth.mx/sitio/index.php?option=com_content&task=category&sectionid=6&id=26&Itemid=56)


Para ejecutarlo:

    $ python sim_tarea11.py
 



## Introducción

<img src="clases_objetos.png">




## Simulación de un Proceso y un Procesador

```python
# coding: utf-8
# Esta simulación muestra el uso de un entorno con un sólo CPU y un sólo proceso.


from fake_scheduler import *
from time import sleep

# Entorno
e = Entorno()

# el entorno 1 sólo procesador, 
e.procesadores = [ Procesador(tiempo_cambio = 2, # cuyo tiempo de cambio de contexto es 2
			      quantum       = 4) # quantum de 4 unidades de tiempo
	       ]



# en el queue hay un sólo proceso
queue = [
    # el proceso con el PID=A
    Proceso("A",
            duracion=7, # debe durar 7 unidades   <--- aguas
            inicio=3,   # pero no puede empezar antes de que t=3
            bloqueos=1, # puede bloquearse, al azar, una vez
            tiempo_bloqueo=2), # si se bloquea, será por dos unidades de tiempo
    ]

# mientras haya procesos en el queue
while queue:    
    # dar cada proceso al despachador, ya se verá si corre
    for p in queue:
        e.despacha(p)
        
    # imprime qué procesador esta ejecutando qué proceso
    print(e)  # la clase Entorno tiene un método para representarse como string

    # el tiempo pasa, actualiza estado de procesadores y procesos
    e.ejecuta()
    
    # quita procesos terminados del queue
    for p in queue:
        if p.status == 'F':
            del(queue[queue.index(p)])


```

Tras ejecutar la simulación con este comando:

```
$ python simulacion_1proceso_1cpu.py
```

Se despliega la siguiente tabla.

```
0 [<cpu idle>]
1 [<cpu idle>]
2 [<cpu idle>]
3 [<cpu R (pid=A st=R d=7 t=0 d-t=7)>]
4 [<cpu R (pid=A st=R d=7 t=1 d-t=6)>]
5 [<cpu R (pid=A st=B d=7 t=2 d-t=5)>]
6 [<cpu R (pid=A st=B d=7 t=2 d-t=5)>]
7 [<cpu TCT>]
8 [<cpu TCT>]
9 [<cpu R (pid=A st=R d=7 t=2 d-t=5)>]
10 [<cpu R (pid=A st=R d=7 t=3 d-t=4)>]
11 [<cpu R (pid=A st=R d=7 t=4 d-t=3)>]
12 [<cpu R (pid=A st=R d=7 t=5 d-t=2)>]
13 [<cpu TCT>]
14 [<cpu TCT>]
15 [<cpu R (pid=A st=R d=7 t=6 d-t=1)>]
```

El proceso "A" empieza hasta t=3, cuando su status cambia a R. Antes
de esto el Procesador está en estado "idle".

En t=5 el proceso "A" se bloquea por dos unidades de tiempo, hasta
t=6.

En t=7 el procesador echa al proceso A cuando se acaba el quantum de 4
unidades, cambia a estado TCT por 2 unidades y mientras no admite
nuevos procesos.

Luego en t=9 le despachan otra vez el proceso "A" y corre sin
interrupción hasta que se le acaba otra vez el quantum en t=13.

Después de otras dos unidades de estado TCT, termina finalmente la
simulación en el t=15.
