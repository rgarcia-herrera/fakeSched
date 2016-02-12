from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String, Float, Boolean
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base
import random

Base = declarative_base()


class Scheduler:

    __tablename__ = 'sched'
    
    def __init__(self, session): #, cpus, processes):
        self.cpus      = []
        self.processes = []
        self.session   = session

    def get_job_to_run(self):
        # order by priority
        # order by wait time
        # order by length
        #session.query(Process).all().order_by()
        return self.session.query(Process).filter_by(running=False).order_by(Process.priority).all()

    def evict_jobs(self,t):
        for job in self.session.query(Process).filter_by(eviction_time = t,
                                                         running       = True).all():
            job.running = False
            job.cpu.running_process = None

    def get_cpu(self):
        return random.choice(self.session.query(Processor).filter_by(running_process=None).all())

    
    def dispatch_jobs(self,t):
        #cpu.log.append([process.ID for n in range(cpu.quantum)])
        #process.length()
        pass

    def pending_jobs(self):
        return False


        
class Processor(Base):
    __tablename__ = 'processor'

    pid = Column(Integer, primary_key=True)
    quantum = Column(Integer)
    running_process = Column(Integer,
                             ForeignKey('process.pid'))
    
    def __init__(self, quantum=1):
        self.quantum = quantum
        self.running = False


    def status(self):
        if self.running_process:
            return "r%s" % self.running_process.pid
        else:
            return "i"


    def run(self, process):
        self.running_process = process
        
    def __repr__(self):
        return "<cpu %s, %s>" % (self.pid, self.status())
        

class Process(Base):
    __tablename__ = 'process'
    
    pid = Column(String, primary_key=True)
    length   = Column(Integer)
    priority = Column(Integer)
    max_wait = Column(Integer)
    waited   = Column(Integer)
    running  = Column(Boolean)
    eviction_time = Column(Integer)
    cpu = Column(Integer,
                 ForeignKey('processor.pid'))

    
    def __init__(self, pid, length, priority, max_wait=3):
        self.pid      = pid
        self.length   = length
        self.priority = priority
        self.max_wait = max_wait
        self.running  = False


    def status(self):
        if self.running:
            return 'r'
        else:
            return 'w'
        
    def __repr__(self):
        return "<job %s, p=%s l=%s s=%s>" % (self.pid, self.priority, self.length, self.status())
        
