import time
import timeit
import random

# give me 8 different numbers between 1 and 10

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

if __name__ == "__main__":
    # Ejecutando las funciones en orden
    start_time = timeit.default_timer()
    a = funcA()
    b = funcB()
    c = funcC(a)
    d = funcD(a, b)
    e = funcE()
    f = funcF(e)
    g = funcG(d)
    h = funcH(d)
    elapsed = timeit.default_timer() - start_time
    print("Tiempo de ejecución: " + str(elapsed))