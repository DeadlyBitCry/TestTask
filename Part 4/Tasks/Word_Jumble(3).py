import random
WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble = ""
tries = 0
hint = word[0:2]
choise = ""
points = 50
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print ( 
"""Добро пожаловать в игру 'Анаграммы'! 
Надо переставить буквы так. чтобы получилось осмысленное слово. 
(Для выхода нажмите Enter. не вводя своей версии.""") 


print("Boт анаграмма: " + jumble)
guess = input("\nПопробуйте отгадать исходное слово: ") 
tries += 1
if guess == correct:
    print ("Верно, вы одгадали слово")
else:
    print("К сожалению, вы неправы.")
while guess != correct: 
    tries +=1
    guess = input("Попробуйте отгадать исходное слово: ")
    if tries > 5:
        while choise != "Y":
            print ("Вы хотите получить подсказку? Y/N")
            choise = input()
            if choise == "Y" or "y":
                points -= 25
                print ("\nДаю вам подсказку: '" + hint +"' первые 2 буквы слова\n")
                break
            break
        break
    elif guess == correct:
        print("Дa. именно так! Вы отгадали!\n")
if points == 50:
    print("Вы получили " + str(points) + " очков")
else:
    print("Вы получили " + str(points) + " очков")
# Доработайте игру «Анаграммы» так, чтобы к каждому слову полаrалась подсказка. 
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой бы иrроки, опадавшие слово без подсказки, получали больше тех, кто запросил подсказку. 
