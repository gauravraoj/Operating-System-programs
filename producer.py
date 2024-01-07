from threading import *
from time import *
from queue import *
q=Queue()
def producer(q):
    i=1
    while True:
        q.put(i)
        print('Producer',i)
        sleep(1)
        i+=1
def consumer(q):
    while True:
        x=q.get()
        print('consumer ',x)
        sleep(1)


t1=Thread(target=lambda :producer(q))
t2=Thread(target=lambda :consumer(q))
t1.start()
t2.start()
t1.join()
t2.join()