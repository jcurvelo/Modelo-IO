import time
import timeit
import random
from threading import Thread, Event


# Funciones a ejecutar

def funcA():
    print("funcA")
    time.sleep(1)
    return 1

def funcB():
    print("funcB")
    time.sleep(3)
    return 3

def funcC(paramFnA):
    print("funcC")
    time.sleep(2)
    return 2

def funcD(paramFnA, paramFnB):
    print("funcD")
    time.sleep(6)
    return 6

def funcE():
    print("funcE")
    time.sleep(2)
    return 2

def funcF(paramFnE):
    print("funcF")
    time.sleep(3)
    return 3

def funcG(paramFnD):
    print("funcG")
    time.sleep(5)
    return 5

def funcH(paramFnD):
    print("funcH")
    time.sleep(1)
    return 1

# Eventos y variables para la sincronización de los hilos
eventA = Event()
eventD = Event()
valorA = 0
valorD = 0

class Hilo1(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        e = funcE()
        f = funcF(e)

class Hilo2(Thread):
    def __init__(self,valorA):
        Thread.__init__(self)
        self.valorA = valorA
        self.start()
    def run(self):
        a = funcA()
        funcC(a)
        self.valorA = a
        eventA.set()

class Hilo3(Thread):
    def __init__(self,valorA,valorD):
        Thread.__init__(self)
        self.valorA = valorA
        self.valorD = valorD
        self.start()
    def run(self):
        b = funcB()
        # La función B se ejecuta en paralelo con la función A, más 
        # la función D debe esperar a que la función A termine
        eventA.wait()
        d = funcD(self.valorA, b)
        self.valorD = d
        eventD.set()


# Los hilos 4 y 5 se ejecutan en paralelo, pero ambos deben esperar a que la función D termine
class Hilo4(Thread):
    def __init__(self,valorD):
        Thread.__init__(self)
        self.valorD = valorD
        self.start()
    def run(self):
        eventD.wait()
        funcG(self.valorD)

class Hilo5(Thread):
    def __init__(self,valorD):
        Thread.__init__(self)
        self.valorD = valorD
        self.start()
    def run(self):
        eventD.wait()
        funcH(self.valorD)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    
    t1 = Hilo1()
    t2 = Hilo2(valorA)
    t3 = Hilo3(valorA,valorD)
    t4 = Hilo4(valorD)
    t5 = Hilo5(valorD)
    
    # Join es usado para esperar a que todos los hilos terminen
    t2.join()
    t1.join()
    t3.join()
    t4.join()
    t5.join()



    elapsed = timeit.default_timer() - start_time
    print("Tiempo de ejecución: " + str(elapsed))