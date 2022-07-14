geek = {"404" : "Не знать. не владеть информацией. От сообщения об ошибке 404 'Стра­ница не найдена'.", 
"Googling": "'Гугление·. nоиск в Сети сведений о ком-либо.", 
"Keyboard Plaque" : "Мусор. который скапливается в клавиатуре компьютера.", 
"Link Rot" : "Процесс устаревания гиперссылок на веб-страницах . ", 
"Percussive Maintenance" : "О ситуации. когда кто-либо бьет по корпусу неисправного электронного прибора в надежде восстановить его работу.", 
"Uninstalled" : "Об увольнении кого-либо. Особенно популярно на рубеже "}
choice = None 
while choice != "0": 
    print("""
    Переводчик с гикского на русский 
    0 - Выйти 
    1 - Найти толкование термина 
    2 - Добавить термин 
    3 - Изменить толкование 
    4 - Удалить термин 
    """)
    choiсе = input(" Ваш выбор: ")  
    print ()  
    if choice == "0": 
        print("Дo свидания.")
    elif choiсе == "1" : 
        term = input("Kaкoй термин вы хотите перевести с гикского на русский? ") 
        if term in geek: 
            definition = geek[term]
            print("\n"+ term + "означает"+ definition)
        else: 
            print("\nУвы. этот термин мне незнаком:", term)
    elif choice == "2": 
        term = input("Kaкoй термин гикского языка вы хотите добавить? ") 
        if term not in geek: 
            definition = input("\nВпишите ваше толкование: ") 
            geek[term] = definition 
            print("\nTepмин" + term + "добавлен в словарь.") 
        else:
            print("\nTaкoй термин уже есть! Попробуйте изменить его толкование.")
    elif choice == "З": 
        term = input("Kaкoй термин вы хотите переопределить? ") 
        if term in geek: 
            definition = input("Впишите ваше толкование: ") 
            geek[term] = definition 
            print("\nTepмин"+ term + "переопределен.") 
        else: 
            print("\nTaкoгo термина пока нет! Попробуйте добавить его в словарь.")
    elif choice == "4": 
        term = input("Kaкoй термин вы хотите удалить? ") 
        if term in geek: 
            del geek[term] 
            print("\nTepмин" + term + "удален.") 
        else: 
            print("\nHичeм не могу помочь, термина"+ term + "нет в словаре.")
    else: 
        print("Извините, в меню нет пункта"+ choice) 
        input("\n\nHaжмитe Enter. чтобы выйти.")