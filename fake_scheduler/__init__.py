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
            p.procesa()
        self.t+= 1


    def __repr__(self):
        return "%s %s" % (self.t, [p for p in self.procesadores])
        
class Procesador(object):
    def __init__(self):
        self.proceso = None

    def procesa(self):
        if self.proceso:
            if self.proceso.duracion > 0:
                self.proceso.duracion -= 1
            else:
                self.proceso.status = 'F'
                self.proceso = None

    def __repr__(self):
        if self.proceso:
            return "<cpu pid=%s>" % self.proceso.pid
        else:
            return "<cpu idle>"
        

class Proceso(object):
    def __init__(self, pid, duracion, inicio):
        self.pid      = pid
        self.duracion = duracion
        self.inicio   = inicio
        self.status   = None

    def __repr__(self):
        return "<p %s %s>" % (self.pid, self.status)
