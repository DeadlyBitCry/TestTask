skills = 30
might = 0
health = 0
wisdom = 0
agility = 0
choice = None
choice2 = None
while skills > 0:
    print("""
    У вас ещё """+ str(skills) + """ очков
    Что бы вы изменить?
    1.Сила ("""+ str(might) + """)
    2.Здоровье (""" + str(health) + """)
    3.Мудрость (""" + str(wisdom) + """)
    4.Ловкость (""" + str(agility) + """)
    5.Завершить изменение характеристик
    """)
    choice = int(input("Ваш выбор:" ))
    if choice == 1:
        if might > 0:
            print("""
            1.Увеличить
            2.Уменьшить
            """)
            choice2 = int(input("Вы хотите увеличить, или уменьшить? "))
            if choice2 == 1:
                amount = input("Сколько очков вы хотите добавить к силе? ")
                might += int(amount)
                skills -= int(amount)
            elif choice2 == 2:
                amount = input("Сколько очков вы хотите отнять от силы? ")
                might -= int(amount)
                skills += int(amount)
            else:
                print("Вы ввели неверное число")
        else:
            amount = input("Сколько очков вы хотите добавить к силе? ")
            might += int(amount)
            skills -= int(amount)
    elif choice == 2:
        if health > 0:
            print("""
            1.Увеличить
            2.Уменьшить
            """)
            choice2 = int(input("Вы хотите увеличить, или уменьшить? "))
            if choice2 == 1:
                amount = input("Сколько очков вы хотите добавить к здоровью? ")
                health += int(amount)
                skills -= int(amount)
            elif choice2 == 2:
                amount = input("Сколько очков вы хотите отнять от здоровья? ")
                health -= int(amount)
                skills += int(amount)
            else:
                print("Вы ввели неверное число")
        else:
            amount = input("Сколько очков вы хотите добавить к здоровью? ")
            health += int(amount)
            skills -= int(amount)
    elif choice == 3:
        if wisdom > 0:
            print("""
            1.Увеличить
            2.Уменьшить
            """)
            choice2 = int(input("Вы хотите увеличить, или уменьшить? "))
            if choice2 == 1:
                amount = input("Сколько очков вы хотите добавить к мудрости? ")
                wisdom += int(amount)
                skills -= int(amount)
            elif choice2 == 2:
                amount = input("Сколько очков вы хотите отнять от мудрости? ")
                wisdom -= int(amount)
                skills += int(amount)
            else:
                print("Вы ввели неверное число")
        else:
            amount = input("Сколько очков вы хотите добавить к мудрости? ")
            wisdom += int(amount)
            skills -= int(amount)
    if choice == 4:
        if agility > 0:
            print("""
            1.Увеличить
            2.Уменьшить
            """)
            choice2 = int(input("Вы хотите увеличить, или уменьшить? "))
            if choice2 == 1:
                amount = input("Сколько очков вы хотите добавить к ловкости? ")
                agility += int(amount)
                skills -= int(amount)
            elif choice2 == 2:
                amount = input("Сколько очков вы хотите отнять от ловкости? ")
                agility -= int(amount)
                skills += int(amount)
            else:
                print("Вы ввели неверное число")
        else:
            amount = input("Сколько очков вы хотите добавить к ловкости? ")
            agility += int(amount)
            skills -= int(amount)
    elif choice == 5:
        break
    else:
        print("Вы ввели неверное число")
# Напишите программу «Генератор персонажей» для ролевой игры.
#  Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость и Ловкость.
# Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пула»,
#  но и возвращать их туда из характеристик, которым он решит присвоить другие значения. 