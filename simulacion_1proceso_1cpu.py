# coding: utf-8
# Esta simulación muestra el uso de un entorno con un sólo CPU y un sólo proceso.


from fake_scheduler import *
from time import sleep

# Entorno
e = Entorno()

# el entorno 1 sólo procesador, cuyo quantum es de 4 unidades de tiempo
e.procesadores = [ Procesador(tiempo_cambio=2, quantum=4), ]



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
    print(e)

    # el tiempo pasa, actualiza estado de procesadores y procesos
    e.ejecuta()
    
    # quita procesos terminados del queue
    for p in queue:
        if p.status == 'F':
            del(queue[queue.index(p)])

