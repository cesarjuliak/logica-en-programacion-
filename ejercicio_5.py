#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de pitagoras: c**2= a**2+b**2    
a = float(input("Ingrese la longitud del cateto a: "))
b = float(input("Ingrese la longitud del cateto b: "))

c = (a**2 + b**2)**0.5


print("El largo de la hipotenusa es: ", c)  