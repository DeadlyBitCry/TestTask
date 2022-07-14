health = 10 
trolls = 0 
damage = 3 
while health > 0 :
    trolls += 1 
    health -= damage
    print("Взмахнув мечом. ваш герой истребляет злобного тролля. " +
    "но сам получает повреждений на " + str(damage) + " очков. \n") 
    print( "Ваш герой доблестно сражался и убил " + str(trolls) + " троллей.") 
print("Ho увы! Он пал на поле боя ") 