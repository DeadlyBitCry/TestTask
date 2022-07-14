inventory = ["меч", "кольчуга", "щит", "целебное снадобье"] 
print("\nИтaк. в вашем арсенале:") 
for item in inventory: 
    print (item) 
input ( "\nНажмите Enter. чтобы продолжить.")
print ("Сейчас в вашем распоряжении "+ str(len(inventory))+ " предмета/ -ов. ") 
input ( "\nНажмите Enter. чтобы продолжить.")
if "целебное снадобье" in inventory:
    print("Вы ещё поживёте и повоюете")
index = int(input("\nBвeдитe индекс одного из предметов арсенала: ")) 
print ("Под индексом "+ str(index) + " в арсенале находится " + inventory[index])
start = int(input("\nBвeдитe начальный индекс среза: ")) 
finish = int(input("Bвeдитe конечный индекс среза: ")) 
print("Cpeз inventory[" + str(start) +":" + str(finish) + "] - это", end=" ") 
print(inventory[start:finish]) 
input("\nHaжмитe Enter. чтобы продолжить.")
chest = ["золото", "драгоценные камни"] 
print("Bы нашли ларец. Вот что в нем есть:") 
print(chest) 
print("Bы приобщили содержимое ларца к своему арсеналу.") 
inventory += chest 
print ("Теперь в вашем распоряжении: ") 
print (inventory) 
input("\n\nHaжмитe Enter. чтобы продолжить.")
print("Bы обменяли меч на арбалет.") 
inventory[0] = "арбалет" 
print("Teпepь ваш арсенал содержит следующие предметы:") 
print (inventory) 
input("\nHaжмитe Enter. чтобы продолжить.")
print("Зa золото и драгоценные камни вы купили магический кристалл, способный пред­сказывать будущее.") 
inventory[4:6] = ["магический кристалл"] 
print("Teпepь в вашем распоряжении:") 
print (inventory)
input("\nHaжмитe Enter. чтобы продолжить.")
print("B тяжелом бою был раздроблен ваш щит.") 
del inventory[2] 
print("Boт что осталось в арсенале:") 
print(inventory) 
input("\nHaжмитe Enter. чтобы продолжить.")
print("Bopы лишили вас арбалета и кольчуги.") 
del inventory[:2] 
print("B арсенале теперь только:") 
print(inventory) 
input("\n\nНажмите Enter. чтобы выйти.")