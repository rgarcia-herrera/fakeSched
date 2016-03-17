import random


class Entorno(object):
    def __init__(self, procesadores=[]):
        self.procesadores = procesadores
        self.t            = 0

    def despacha(self, proceso):
        for cpu in self.procesadores:
            if cpu.status == 'idle':
                if self.t >= proceso.inicio and proceso.status != 'R':
                    cpu.proceso    = proceso
                    cpu.status     = 'R'
                    proceso.status = 'R'
                    break
            

    def ejecuta(self):
        for p in self.procesadores:
            p.procesa()
        self.t+= 1


    def __repr__(self):
        return "%s %s" % (self.t, [p for p in self.procesadores])
        
class Procesador(object):
    def __init__(self, cambio=10, bloqueo=10):
        self.cambio  = cambio
        self.bloqueo = bloqueo
        self.proceso = None
        self.status  = 'idle'
        self.tct     = cambio

    def procesa(self):
        if self.status == 'TCT':
            self.tct -= 1
            if self.tct == 0:
                self.status = 'idle'
                self.tct = self.cambio

            
        elif self.proceso:                    
            if self.proceso.tiempo_de_ejecucion < self.proceso.duracion and self.proceso.status != 'B':
                self.statsus = 'R'
                self.proceso.tiempo_de_ejecucion += 1
            else:
                self.proceso.status = 'F'
                self.proceso = None
                # al terminar un proceso hay que entrar en tiempo de cambio de contexto
                self.status  = 'TCT'

    def __repr__(self):
        if self.proceso:
            return "<cpu %s %s>" % (self.status, self.proceso)
        else:
            return "<cpu %s>" % self.status
        

class Proceso(object):
    def __init__(self, pid, duracion, inicio, bloqueos):
        self.pid      = pid
        self.duracion = duracion
        self.inicio   = inicio
        self.bloqueos = bloqueos
        self.tiempo_de_ejecucion = 0
        self.status   = None

    def __repr__(self):
        return "(pid=%s st=%s pendiente=%s)" % (self.pid, self.status, self.duracion-self.tiempo_de_ejecucion)
