numero= int(input("ingresa un numero de tres digitos: "))
rev= "".join(reversed(str(numero)))
rever=int(rev)

if numero == rever:
    print("es palindromo")
else :
    print("no es palindromo")







