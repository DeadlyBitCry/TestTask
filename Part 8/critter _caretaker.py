# Моя зверюшка 
# Виртуальный питомец. о котором пользователь может заботиться 
class Critter(object): 
    """Виртуальный питомец""" 
    def __init__(self , name, hunger = 0, boredom = 0): 
        self.name = name 
        self.hunger = hunger 
        self.boredom = boredom
    def __pass_time(self): 
        self.hunger += 1 
        self.boredom += 1
    @property 
    def mood(self): 
        unhappiness = self.hunger + self.boredom 
        if unhappiness < 5: 
            m = "прекрасно" 
        elif 5 <= unhappiness <= 10:
            m = "неплохо" 
        elif 11 <= unhappiness <= 15: 
            m = "не сказать чтобы хорошо" 
        else:
            m = "ужасно" 
        return m
    def talk(self):
        print("Meня зовут " + self.name + ", и сейчас я чувствую себя " + self.mood + " сейчас.\n") 
        self.__pass_time()
    def eat(self,food = 4):
        print("Сколько еды вы хотите дать зверьку? ")
        amount_food = int(input()) 
        print("Мррр... Спасибо!") 
        self.hunger = food - amount_food 
        if self.hunger < 0: 
            self.hunger = 0 
        self.__pass_time()
    def play(self, fun = 4):
        print("Сколько часов вы хотите с ним поиграть? ")
        playtime = int(input())
        print("Уиии!") 
        self.boredom = fun - playtime
        if self.boredom < 0: 
            self.boredom = 0 
        self.__pass_time()
    def __str__(self):
        print("Зверюшка имеет " + str(self.hunger) +" Голода")
        print("И " + str(self.boredom) + " Скуки")
def main(): 
    crit_name = input("Kaк вы назовете свою зверюшку?") 
    crit = Critter(crit_name)
    choice = None 
    while choice !="0": 
        print (""" 
        Моя зверюшка 
        0 - Выйти 
        1 - Узнать о самочувствии зверюшки 
        2 - Покормить зверюшку 
        3 - Поиграть со зверюшкой 
        """) 
        choice = input("Baш выбор: ") 
        print() 
        # ВЫХОД 
        if choice == "0": 
            print("Дo свидания.") 
        # беседа со зверюшкой 
        elif choice == '1':
            crit.talk() 
        # кормление зверюшки 
        elif choice == "2": 
            crit.eat() 
        # игра со зверюшкой 
        elif choice == "3": 
            crit.play()
        elif choice == "cheatcode":
            crit.__str__()
        # непонятный пользовательский ввод 
        else: 
            print( "Извините, в меню нет пункта " + choice)
main() 
input("\n\nHaжмитe Enter, чтобы выйти.")