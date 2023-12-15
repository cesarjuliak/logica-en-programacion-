#funciones
import math
def estimar_pi (n):
    suma= 0
    signo=1
    for i in range(n):
        termino= 1/(2*i+1)
        suma= suma + signo*termino
        signo*=-1
    estimacion_pi=4*suma
    return estimacion_pi
#inicio programa
n= int(input("ingrese el numero del tremino para estimar pi"))
print(estimar_pi(n))






























