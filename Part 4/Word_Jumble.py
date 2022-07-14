import random
#создадим последовательность слов. из которых компьютер будет выбирать 
WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word
jumble = ""
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
while guess != correct and guess != "": 
    print("K сожалению. вы неправы.") 
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == correct: 
    print("Дa. именно так! Вы отгадали!\n")