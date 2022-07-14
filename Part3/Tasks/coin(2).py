print("Данная программа бросает монету 100 раз")
import random
orel = 0
reshka = 0
amount = 0
while amount < 100:
    throw = random.randint(1 , 2)
    if throw == 1:
        orel += 1
    elif throw == 2:
        reshka += 1
    amount += 1
print("Орёл выпал " + str(orel) + " раз")
print("Решка выпала " + str(reshka) + " раз")
# Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и сообщала, сколько раз выпал 
#орел, а сколько - решка. 