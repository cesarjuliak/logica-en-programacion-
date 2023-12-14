#perimetro = 2(pi) por radio . area = pi por radio al cuadrado

import math

radio= float (input ("ingrese el valor del radio"))
perimetro =2*math.pi*radio 
perimetro= "{: .3f}". format(perimetro)
area= math.pi*radio**2
area= "{:.2f}". format(area)    


print ("el perimetro es : " +str ( perimetro) )
print ("el area es : " +str (area) )    

































