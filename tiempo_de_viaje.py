#desarrolle un programa que permta ingresar los tiempos de viaje de los tramos y entregue 
#como resultado el tiempo total del viaje en formato horas minutos 

tiempo_viaje= int(input("ingresa el tiempo de viaje en minutos: "))
tiempo= tiempo_viaje
while tiempo_viaje!=0:
    tiempo_viaje= int(input("ingresa el tiempo de viaje en minutos: "))
    tiempo= tiempo + tiempo_viaje
print(tiempo)
horas= int(tiempo/60)
minutos =tiempo % 60
print(f"{horas}:{minutos}")

















