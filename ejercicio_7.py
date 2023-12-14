#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

numero = float(input("Ingrese un número real: "))
import math
decimal=0
if numero <0:
    decimal=math.modf(numero)
    print("La parte decimal es: ", {decimal})
else:
    print("La parte decimal es: ", numero%1)
