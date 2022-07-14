import random
diel = random.randint(1, 6)
die2 = random.randrange(6) + 1 
total = diel + die2
print("Сумма 1-го кубика = " + str(diel) + (" Сумма 2-го кубика = " + str(die2) + " Общая сумма = " + str(total)))