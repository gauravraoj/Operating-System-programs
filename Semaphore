from threading import *
from time import *
def display(str1):
    l.acquire()
    for x in str1:
        print(x)
    l.release()
l=Semaphore(2)
t1=Thread(target=display, args=('Helo world',))
t2=Thread(target=display, args=('HELLO are gaurav',))

t3=Thread(target=display, args=('0123456789',))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
