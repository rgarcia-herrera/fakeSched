import random


class Entorno(object):
    def __init__(self, cambio=10, bloqueo=10, procesadores=[]):
        self.cambio       = cambio
        self.bloqueo      = bloqueo
        self.procesadores = procesadores
        self.t            = 0

    def despacha(self, proceso):
        for p in self.procesadores:
            if p.proceso == None:
                if self.t >= proceso.inicio and proceso.status != 'R':
                    p.proceso = proceso
                    proceso.status = 'R'
                    break
            

    def ejecuta(self):
        for p in self.procesadores:
            p.procesa(bloqueo=self.bloqueo)
        self.t+= 1


    def __repr__(self):
        return "%s %s" % (self.t, [p for p in self.procesadores])
        
class Procesador(object):
    def __init__(self):
        self.proceso = None

    def procesa(self, bloqueo):
        if self.proceso:
            # if self.proceso.bloqueos > 0:
            #     if random.choice([True, False]):
            #         self.proceso.status = 'B'
            #         self.proceso.bloqueos -= 1
                    
            if self.proceso.tiempo_de_ejecucion < self.proceso.duracion and self.proceso.status != 'B':
                self.proceso.tiempo_de_ejecucion += 1
            else:
                self.proceso.status = 'F'
                self.proceso = None

    def __repr__(self):
        if self.proceso:
            return "<cpu pid=%s>" % self.proceso.pid
        else:
            return "<cpu idle>"
        

class Proceso(object):
    def __init__(self, pid, duracion, inicio, bloqueos):
        self.pid      = pid
        self.duracion = duracion
        self.inicio   = inicio
        self.bloqueos = bloqueos
        self.tiempo_de_ejecucion = 0
        self.status   = None

    def __repr__(self):
        return "<p %s %s d%s e%s>" % (self.pid, self.status, self.duracion, self.tiempo_de_ejecucion)
