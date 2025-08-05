import math
ca = int(input("Digite o valor do cateto adjacente: "))
co = int(input('Digite o valor do cateto oposto: '))
#hip = math.sqrt((pow(ca,2))+pow(co,2))
#print(hip)
hip2 = math.hypot(ca,co)
print(hip2)
