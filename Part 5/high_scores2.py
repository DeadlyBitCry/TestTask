scores = [] 
choice = None
while choice != "0": 
    print("""
    Рекорды 2.0
    О - Выйти 
    1 - Показать рекорды 
    2 - Добавить рекорд
    """) 
    choice = input("Baш выбор: ") 
    print ()
    if choice == "0": 
        print ("До свидания.")
    elif choice == "1": 
        print("Peкopды\n") 
        print ("ИМЯ\tРЕЗУЛЬТАТ") 
        for entry in scores: 
            score , name = entry 
            print(name, "\t", score)
    elif choice == "2": 
        name = input("Впишите имя игрока: ") 
        score = int(input("Bnишитe его результат: ")) 
        entry = (score, name) 
        scores.append(entry) 
        scores.sort(reverse=True) 
        scores = scores[:5]
    else: 
        print("Извините. в меню нет пункта", choice)