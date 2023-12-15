# escriba un programa que reciba como entrada fos numeros, y los muestre ordenados 
# de menor a mayor
num1= int(input("ingresa un numero: "))
num2= int(input("ingresa otro numero: "))
if num1 > num2 :
    print (f"{num2} {num1}")
elif num2 > num1 :
    print (f"{num1} {num2}")

print ("ahora lo haremos con tres numeros")
num1= int(input("ingresa un numero: "))
num2= int(input("ingresa otro numero: "))
num3= int(input("ingresa otro numero: "))

numeros= [num1, num2, num3]
ordenados = sorted(numeros)  #sorted ordena la lista de modo ascendente 
print (ordenados)

print ("ahora lo haremos con cuatro numeros")
num1= int(input("ingresa un numero: "))
num2= int(input("ingresa otro numero: "))
num3= int(input("ingresa otro numero: "))
num4= int(input("ingresa otro numero: "))
numeros= [num1, num2, num3,num4]
ordenados = sorted(numeros)
print (ordenados)












