# coding: utf8

from fake_scheduler import *
from time import sleep

# Entorno 2
e2 = Entorno()

# el entorno 2 tiene dos procesadores
e2.procesadores = [ Procesador(tiempo_cambio=2, quantum=4), ]
#                    Procesador(tiempo_cambio=3, quantum=3) ]



queue = [
    Proceso("A", duracion=7,  inicio=3, bloqueos=1, tiempo_bloqueo=2),
#    Proceso("B", duracion=6,  inicio=0, bloqueos=2, tiempo_bloqueo=5),
#    Proceso("C", duracion=4,  inicio=0, bloqueos=2, tiempo_bloqueo=5),
    # Proceso("D", duracion=100,  inicio=0,    bloqueos=2),
    # Proceso("E", duracion=1000, inicio=3000, bloqueos=5),
    # Proceso("F", duracion=500,  inicio=0,    bloqueos=3),
    # Proceso("G", duracion=10,   inicio=3000, bloqueos=2),
    # Proceso("H", duracion=700,  inicio=0,    bloqueos=4),
    # Proceso("I", duracion=450,  inicio=3000, bloqueos=3),
    # Proceso("J", duracion=300,  inicio=1500, bloqueos=2),
    # Proceso("K", duracion=100,  inicio=4000, bloqueos=2),
    # Proceso("L", duracion=3000, inicio=1500, bloqueos=5),
    # Proceso("M", duracion=80,   inicio=4000, bloqueos=2),
    # Proceso("N", duracion=50,   inicio=1500, bloqueos=2),
    # Proceso("Ñ", duracion=500,  inicio=8000, bloqueos=3),
    # Proceso("O", duracion=600,  inicio=1500, bloqueos=3),
    # Proceso("P", duracion=800,  inicio=4000, bloqueos=4),
    ]

# mientras haya procesos en el queue

while queue:    
    # dar cada proceso al despachador, ya se verá si corre
    for p in queue:
        e2.despacha(p)
        
    # imprime qué procesador esta ejecutando qué proceso
    print(e2)

        
    # el tiempo pasa, actualiza estado de procesadores y procesos
    e2.ejecuta()


    
    # quita procesos terminados del queue
    for p in queue:
        if p.status == 'F':
            del(queue[queue.index(p)])

    sleep(0.001)
