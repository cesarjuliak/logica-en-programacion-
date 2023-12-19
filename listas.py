#un algoritmo que muestra algunas funciones de las listas 

numeros=[1,3,2,4,5]
print(numeros.index(1)) # index busca la posicion de un numero dentro de la lista
print (sum(numeros)) # sum suma los numeros dentro de la lista

numeros.sort() #sort ordena una lista de numeros
print(numeros) 

num=[x+1 for x in range (100)]
print(num ) 

num=[x for x in range(100) if x%2==0 ] 
print(num )

nombres=["camilo","juan","pedro","mario","jose"]

#imprime los que cumplen la condicion dentro de la lista 
nuevos_nombres=[name for name in nombres if len(name)>5]

print(nuevos_nombres) 



