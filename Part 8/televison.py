class Television (object):
    """Телевизор"""
    def __init__(self, channel = 0, volume = 0):
        self.channel = channel
        self.volume = volume
    def change_channel (self):
        print("Какой канал вы хотите включить?(У вас их 100) ")
        self.channel = int(input())
        while self.channel > 100 or self.channel < 0:
            print("У вас нет такого канала")
            break;
    def change_volume (self):
        print("Сейчас громкость равна " + str(self.volume) + ". Вы хотите уменьшить или прибавить звук?(Выберите 1 или 2 соответственно) ")
        plus_or_minus = int(input())
        print ("Насколько вы хотите поменять громкость? ")
        volume_amount = int(input())
        if plus_or_minus == 1:
            self.volume -= volume_amount
            if self.volume < 0:
                self.volume = 0
        elif plus_or_minus == 2:
            self.volume += volume_amount
            if self.volume > 100:
                self.volume = 100
        else:
            print("Такой кнопки у вас нет")
def main():
    object_name = "Televizor"
    tv = Television(object_name)
    choice = None
    print("Вы включили телевизор")
    while choice != '0':
        print (""" 
        Настройки
        0 - Выключить телевизор 
        1 - Переключить канал
        2 - Поменять громкость
        """) 
        choice = input("Что вы хотите сделать? ")
        if choice == '0':
            print("Телевизор выключается")
        elif choice == '1':
            tv.change_channel()
        elif choice == '2':
            tv.change_volume()
        else:
            print("Такой функции нет, простите")
main()
input("Нажмите Enter, чтобы выйти")