# coding: utf-8

from fake_scheduler import *
from time import sleep



e = Entorno()


# el entorno tiene 2 procesadores con diferentes quanta
e.procesadores = [ Procesador(tiempo_cambio = 2,
                              quantum       = 3000),
                   Procesador(tiempo_cambio = 2,
                              quantum       = 5),
               ]



queue = [
    Proceso("A", duracion=20,
            inicio=3,  
            bloqueos=2, tiempo_bloqueo=1),
    Proceso("B", duracion=10,
            inicio=0,  
            bloqueos=0),
    Proceso("C", duracion=15,
            inicio=0,  
            bloqueos=1, tiempo_bloqueo=2),
    Proceso("D", duracion=4,
            inicio=5,  
            bloqueos=0)

]




while queue:    

    for p in queue:
        e.despacha(p)
        

    print(e)

    e.ejecuta()

    
    # quita procesos terminados del queue
    for p in queue:
        if p.status == 'F':
            del(queue[queue.index(p)])
