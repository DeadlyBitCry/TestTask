# Зверюшка с конструктором 
# Демонстрирует метод-конструктор 
class Critter(object): 
    """Виртуальный питомец""" 
    def __init__ (self,name): 
        print("Появилась на свет новая зверюшка!") 
        self.name = name
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep
    def talk(self): 
        print("\nПpивeт. Меня зовут " + self.name +  "\n") 
# основная часть 
crit1 = Critter("Бoбик") 
crit1.talk() 
crit2 = Critter( "Мурзик") 
crit2.talk() 
print("Bывoд объекта crit1 на экран:") 
print(crit1) 
print("Непосредственный доступ к атрибуту critl.name:") 
print(crit1.name) 
input("\n\nHaжмитe Enter. чтобы выйти.")