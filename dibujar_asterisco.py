# escriba in programa que pida al usuario ingresar la altura y el ancho de un rectangulo y lo
# dibuje utilizando asteriscos 
#funcion
def dibujar_rectangulo(ancho, altura):
    for i in range(altura):
        for j in range(ancho):
            print("*", end="")
        print() # salto de linea despues de cada fila 

#algoritmo
ancho= int(input("ingrese el ancho del rectangulo: "))
altura= int(input("ingrese la altura del rectangulo: "))
print (dibujar_rectangulo(ancho, altura))

#dibujar un triangulo 
def dibujar_triangulo(altura):
    






















