import random
print( "\tДобро пожаловать в игру 'Отгадай число'!") 
print("\nЯ загадал натуральное число из диапазона от 1 до 100.") 
print("Постарайтесь отгадать его за минимальное число попыток.\n")
the_number = random.randint(1 , 100) 
guess = int(input("Baшe предположение: ")) 
tries = 1
while guess != the_number: 
    if guess > the_number: 
        print("Меньше") 
    else: 
        print( "Больше.") 
    guess = int((input("Ваше предположение: ")))
    tries += 1
print("Baм удалось отгадать число! Зто в самом деле " + str(the_number)) 
print("Bы затратили на отгадывание всего лишь " , str(tries) , " попыток!\n")