# Классово верная зверюшка 
# Демонстрирует атрибуты класса и статические методы 
class Critter(object): 
    """Виртуальный питомец""" 
    total = 0 
    @staticmethod 
    def status(): 
        print("\nBcero зверюшек сейчас" + str(Critter.total)) 
    def __init__ (self, name):
        print("Появилась на свет новая зверюшка!") 
        self.name = name 
        Critter.total += 1 
# основная часть 
print("Haxoжy значение атрибута класса Critter.total:" , end=" ") 
print(Critter.total) 
print("\nCoздaю зверюшек ") 
critl = Critter("зверюшка 1") 
crit2 = Critter("зверюшка 2")
critЗ = Critter("зверюшка 3") 
Critter.status()
print("\nOбpaщaюcь к атрибуту класса через объект:" , end=" ") 
print(critl.total) 
input("\n\nHaжмитe Enter. чтобы выйти.") 