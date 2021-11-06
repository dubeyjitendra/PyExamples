# PYTHON MULTITASKING – MULTITHREADING AND MULTIPROCESSING
# http://devarea.com/python-multitasking-multithreading-multiprocessing/#.XB8K8FwzbIU

# multiprocessing — Process-based parallelism
# https://docs.python.org/3/library/multiprocessing.html

# Multithreading vs Multiprocessing in Python
# https://medium.com/@nbosco/multithreading-vs-multiprocessing-in-python-c7dc88b50b5b


"""1- multitasking: excuting serval task simulteously is called multi tasking
2-Types of Multi Tasking
    1-process based multi tasking
    2-thread based multi multitasking

# https://www.google.com/imgres?imgurl=http://1.bp.blogspot.com/-m5PM7x87SUA/VjjEcezeZ9I/AAAAAAAAEFY/CXAOT6c3Qq0/s1600/Difference%252Bbetween%252Bmultitasking%252Band%252Bmultithreading.jpg&imgrefurl=http://www.java67.com/2015/11/difference-between-multithreading-and-multitasking.html&h=1092&w=1456&tbnid=7tA8Q4WgTWIbUM:&q=Thread+based+multi+tasking&tbnh=160&tbnw=213&usg=AI4_-kTjtWyeepJCkyUTebO2NdJRUy69sQ&vet=1&docid=JYqzi8oiAVVcdM&sa=X&ved=2ahUKEwiEw9_QiLXfAhXDdysKHdKBBlIQ9QEwAHoECAYQBg


1- Process Based Multi threding : Excuting serveral task simulteously where each task is
               separate independent process

1-download movies background - editor realted process
2- write code in editor- related process running
3- listing audio song- audio player process running


this is os level


2- Thread based multi tasking:
Excuting serveral task simulteously where each task is
               separate independent part of same program each independent part is called thread based multi tasking

note: we can reduces exection time and perfomance

# Thread-based multitasking allows a single program to run two or more threads concurrently. 
#Communication between two processes is expensive and limited. ... 
#Context switching from one process to another process is expensive. 
#Context switching from one thread to another thread is less expensive as compared to process


uses of multi threading concept:
1- animation
2- video games
3- multi media graphics
4- web server and application server
impotant notes: 60-70 thread execute simuleously

single thread program : for single thread
one by one execution

thread are flow of execution"""


#Thread Example
"""
3 Ways create thread:

1-creating thread without using class
    2-creating thread by extending class
        3-creating thread by without extending class

"""
#   1 With creating class
from threading import *

"""
def display():
    print("cureent thread",current_thread().getName())

t=Thread(target=display) # main thread responsible for run child thrad
t.start() #main thread child thread
print("cureent thread", current_thread().getName())
"""
"""def display():
    for i in range(10):
        print("current thread")

t=Thread(target=display) # Main Thread
t.start()
for i in range(10):
    print("main thread")"""

#2- extending class
'''from threading import *
class myThread(Thread):
    def run(self):
        for i in range(10):
            print("child-thread-1")

t=myThread()
t.start()
for i in range(10):
    print("main-thread-1")'''

from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("child-thread-2")

obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("main-thread-2")

"""import time

def calc_square(n):
    for row in n:
        time.sleep(0.2)
        print(row *row)

def calc_cube(n):
    for row in n:
        time.sleep(0.2)
        print(row *row*row)


arr=[2,3,4,5]
t=time.time()

calc_square(arr)
calc_cube(arr)

print('done in',time.time()-t)
print('done with all changes')"""

#Multi Thread Example
"""
import time
import threading
def calc_square(n):
    for row in n:
        time.sleep(0.2)
        print(row *row)

def calc_cube(n):
    for row in n:
        time.sleep(0.2)
        print(row *row*row)


arr=[2,3,4,5]
t=time.time()
t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_square,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print('done in',time.time()-t)
print('done with all changes')"""
