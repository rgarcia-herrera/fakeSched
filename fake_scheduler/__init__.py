
import random


class Entorno(object):
    def __init__(self, procesadores=[]):
        self.procesadores = procesadores
        self.t            = 0

    def despacha(self, proceso):
        for cpu in self.procesadores:
            if cpu.status == 'idle':
                if self.t >= proceso.inicio and proceso.status != 'R' and proceso.status != 'B':
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
    def __init__(self, tiempo_cambio=10, quantum=100):
        self.tiempo_cambio  = tiempo_cambio
        self.quantum        = quantum
        self.proceso        = None
        self.status         = 'idle'
        self.tct            = tiempo_cambio
        self.q              = 0

    def procesa(self):
        # en tiempos de cambio de contexto no se procesa nada
        if self.status == 'TCT':
            self.tct -= 1
            if self.tct == 0:
                self.status = 'idle'
                self.tct = self.tiempo_cambio
                
        elif self.proceso and self.status == 'R':
            
            self.proceso.ejecuta()
            
            # contabiliza el quantum
            self.q += 1
            
            # tras ejecutarlo una unidad vemos si no ha terminado
            if self.proceso.status == 'F':
                # quitamos proceso terminado
                self.proceso = None
                # al terminar un proceso hay que entrar en tiempo de cambio de contexto
                self.status  = 'TCT'
            elif self.q >= self.quantum: # habra agotado su quantum?
                # resetea contador de quantum
                self.q = 0
                # proceso en status Wait
                self.proceso.status = 'W'

                # si el proceso es echado por agotamiento de quantum
                # mientras esta bloqueado, hay que regresarle el
                # bloqueo interrumpido
                if self.proceso.status == 'B':
                    self.proceso.bloqueos += 1
                self.proceso = None
                self.status  = 'TCT'

            
                
    def __repr__(self):
        if self.proceso:
            return "<cpu %s %s>" % (self.status, self.proceso)
        else:
            return "<cpu %s>" % self.status
        

class Proceso(object):
    def __init__(self, pid, duracion, inicio, bloqueos, tiempo_bloqueo=10):
        self.pid      = pid
        self.duracion = duracion
        self.inicio   = inicio
        self.bloqueos = bloqueos
        self.tiempo_bloqueo = tiempo_bloqueo        
        self.tiempo_de_ejecucion = 0
        self.tiempo_bloqueado    = 0
        self.status   = 'W'

    def __repr__(self):
        return "(pid=%s st=%s d=%s t=%s d-t=%s)" % (self.pid, self.status, self.duracion,
                                                    self.tiempo_de_ejecucion, self.duracion-self.tiempo_de_ejecucion)


    def ejecuta(self):
        
        if self.status == 'R':
            # mientras estE corriendo y queden bloqueos pendientes,
            # tal vez hay que bloquear
            if self.bloqueos > 0 and random.choice([True, False]):
                self.bloqueos -= 1
                self.status = 'B'                
                self.tiempo_bloqueado = 0
            else:
                # ejecucion normal
                self.tiempo_de_ejecucion += 1
                
                # si se alcanzo el tiempo solicitado, marcar como Finalizado
                if self.tiempo_de_ejecucion == self.duracion:
                    self.status = 'F'


        # si el proceso esta bloqueado aumentar el contador de bloqueo
        if self.status == 'B':
            self.tiempo_bloqueado += 1

            # si alcanzo el tiempo de bloqueo, desbloquear
            if self.tiempo_bloqueado > self.tiempo_bloqueo:
                self.status = 'R'
