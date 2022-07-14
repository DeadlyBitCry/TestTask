def birthday1(name, age): #Позиционные параметры
    print( "С днем рождения, "+ str(name) + "!"+ " Вам сегодня исполняется "+ str(age) + " не так ли? \n")  
def birthday2(name = "товарищ Иванов" , age = 1): #Значения параметров по умолчанию
    print( "С днем рождения, " + str(name) + "!"+ " Вам сегодня исполняется " + str(age) + " не так ли? \n") 
birthday1("тoвapищ Иванов ", 1) #Позиционные аргументы
birthday1 (1, " товарищ Иванов ") #Позиционные аргументы
birthday1( name = " товарищ Иванов ", age = 1) 
birthday1(age = 1 , name = " товарищ Иванов ") 
birthday2() 
birthday2(name = "Катя") 
birthday2(age = 12) 
birthday2( name = "Катя" , age = 12) 
birthday2( "Катя" , 12) 
input("\n\nHaжмитe Enter. чтобы выйти.")