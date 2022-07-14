import random
chislo = int(input("Введите загаданное число "))
if chislo > 100 or chislo < 1:
    print("Введено неверное число")
else:
    try_ = 0
    guess = random.randint(1, 100)
    guess2 = 100
    guess3 = 1
    while guess != chislo:
        if guess > chislo:
            guess2 = guess
            guess = random.randint(guess3,guess)
        elif guess < chislo:
            guess3 = guess
            guess = random.randint(guess,guess2)
        try_ += 1
    print("Вы угадали число за " + str(try_) + " попыток")
    print("Это число " + str(chislo))
#вот задача посложнее. Напишите на псевдокоде алгоритм игры, в которой случайное число от 1 до 100 загадывает человек, а отгадывает компьютер.
#Прежде чем приступать к решению, задумайтесь над тем, какой должна быть оптимальная стратегия опадывания.
# Если алгоритм на псевдокоде будет удачным, попробуйте реализовать игру на Pythoп. 