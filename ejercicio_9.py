#escriba un programa que pida al usuario dos palabras, y que indique 
#cual de ellas es la mas larga y por cuantas lo es 
palabra_1= input(("ingrese la primer palabra:"))
palabra_2= input(("ingrese la segunda palabra:"))
longitud_1= len(palabra_1)
longitud_2= len(palabra_2)
if longitud_1>longitud_2:
    diferencia= longitud_1 - longitud_2
    print (f"{palabra_1} es mas larga  que {palabra_2} por {diferencia} letras")
elif longitud_2>longitud_1:
    diferenia= longitud_2 - longitud_1
    print (f"{palabra_2} es mayor que {palabra_1} por {diferenia} letras")






























