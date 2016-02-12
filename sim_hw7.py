from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint
from fake_scheduler import Base, Processor, Process, Scheduler

engine  = create_engine("sqlite://")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)    
session = Session()
    


p1 = Processor(1)
p2 = Processor(1)
p3 = Processor(1)

session.add( p1 )
session.add( p2 )
session.add( p3 )

job1 = Process(pid=1, length=10, priority=0)
job2 = Process(pid=2, length=14, priority=1)
job3 = Process(pid=3, length=50, priority=1)
job4 = Process(pid=4, length=100, priority=2)

session.add(job1)
session.add(job2)
session.add(job3)
session.add(job4)




s = Scheduler(session)
s.cpus = [p1, p2, p3]
s.jobs = [job1, job2, job3, job4]


#session.add(s)
session.commit()
t = 0
while s.pending_jobs():
    s.evict_jobs(t)
    s.dispatch_jobs(t)
    t += 1
