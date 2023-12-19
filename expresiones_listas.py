#considere las siguientes listas 
a=[5,1,4,9,0,]
b=list(range(3,10))+list(range(20,23))
c=[[1,2],[3,4,5],[6,7]]
d=["perro","gato","jirafa","elefante"]
e=["a",a,2*a]
#sin usar el computador, indique cual es el  resultado y el tipo de las siguientes 
#expresiones. a continuacion, verifique sus respuestas en el computador 

print (a[2]) # imprimir el valor de la posision 2 de la lista que inicia en 0 
print (b[9])
print (c[2][1]) # el primero [] busca la posicion de la sublista dentro de c y el segundo[] busca el elemento dentro de la sublista en esa posicion 
print (e[0]==e[1])
print (len(c)) #indica la longitud de la lista en le caso de c, muestra cuantas sub listas tiene
print (c[0])
print (len(e))
print (c[-1]) # indica el ultimo elemento de la lista, en el caso de c, muestra la ultima sub lista 
print(c[-1][+1]) # [-1] indica el ultimo elemento de la lista, en este caso de la lista c, indica la ultima sub lista. [+1] indica el segundo elemento dentro de la sublista 
print(c[2:]+d[2:]) # + une las listas c y d. c[2:] muestra los elementos que siguen apártir de esa posicion  del mismo modo que d[2:]
print (a[3:10]) # imprime los valores en ese rango, si el limite es mayor qu la cantidad de elementos imprime hasta el ultimo 
print(a[3:10:2])
print (d.index("jirafa")) #indica en que posicion esta el elemento 
print (e[c[0][1]].count(5)) # count dice cuantas veces aparce el valor() 
print (sorted(a)[2])
print (complex(b[0],b[1])) # complex crea un numero complejo












