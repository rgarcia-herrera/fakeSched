# coding: utf8

from fake_scheduler import *
from time import sleep


e2 = Entorno()

e2.procesadores = [ Procesador(tiempo_cambio=15, quantum=3000), 
                    Procesador(tiempo_cambio=15, quantum=3000) ]


queue = [
    Proceso("A", duracion=400,  inicio=3000, bloqueos=2, tiempo_bloqueo=10),
    Proceso("B", duracion=300,  inicio=0,    bloqueos=2, tiempo_bloqueo=10),
    Proceso("C", duracion=50,   inicio=3000, bloqueos=2, tiempo_bloqueo=10),
    Proceso("D", duracion=100,  inicio=0,    bloqueos=2, tiempo_bloqueo=10),
    Proceso("E", duracion=1000, inicio=3000, bloqueos=5, tiempo_bloqueo=10), 
    Proceso("F", duracion=500,  inicio=0,    bloqueos=3, tiempo_bloqueo=10),
    Proceso("G", duracion=10,   inicio=3000, bloqueos=2, tiempo_bloqueo=10),
    Proceso("H", duracion=700,  inicio=0,    bloqueos=4, tiempo_bloqueo=10),
    Proceso("I", duracion=450,  inicio=3000, bloqueos=3, tiempo_bloqueo=10),
    Proceso("J", duracion=300,  inicio=1500, bloqueos=2, tiempo_bloqueo=10),
    Proceso("K", duracion=100,  inicio=4000, bloqueos=2, tiempo_bloqueo=10),
    Proceso("L", duracion=3000, inicio=1500, bloqueos=5, tiempo_bloqueo=10),
    Proceso("M", duracion=80,   inicio=4000, bloqueos=2, tiempo_bloqueo=10),
    Proceso("N", duracion=50,   inicio=1500, bloqueos=2, tiempo_bloqueo=10),
    Proceso("Ñ", duracion=500,  inicio=8000, bloqueos=3, tiempo_bloqueo=10),
    Proceso("O", duracion=600,  inicio=1500, bloqueos=3, tiempo_bloqueo=10),
    Proceso("P", duracion=800,  inicio=4000, bloqueos=4, tiempo_bloqueo=10), 
    ]



while queue:    
    for p in queue:
        e2.despacha(p)
        
    print(e2)

    e2.ejecuta()
    
    # quita procesos terminados del queue
    for p in queue:
        if p.status == 'F':
            del(queue[queue.index(p)])

    sleep(0.001)
