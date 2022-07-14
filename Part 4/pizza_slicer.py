print("Для выхода нажмите Enter. не вводя начальную позицию ") 
word = "пицца"
start = None 
while start != "":
    start = (input("\nНачальная позиция: ")) 
    if start: 
        start = int(start) 
        finish = int(input("Koнeчнaя позиция: ")) 
        print("Cpeз word[" , start, ":" , finish , "]выглядит как" , end=" ") 
        print(word[start:finish])