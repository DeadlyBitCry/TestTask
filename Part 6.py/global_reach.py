def read_global(): 
    print( "В области видимости функции read_global () значение value равно " + str(value)) 
def shadow_global(): 
    value = -10 
    print("B области видимости функции shadow_global() значение value равно " + str(value)) 
def change_global(): 
    global value 
    value = -10 
    print("B области видимости функции change_global() значение value равно "+ str(value)) 
value = 10 
print("B глобальной области видимости значение переменной value сейчас стало равным " + str(value) + "\n") 
read_global () 
print ("Вернемся в глобальную область видимости. Здесь value по-прежнему равно "+ str(value) + "\n") 
shadow_global () 
print("Bepнeмcя в глобальную область видимости. Здесь value по-прежнему равно " + str(value)+ "\n") 
change_global () 
print("Bepнeмcя в глобальную область видимости. Значение value изменилось на " + str(value)) 
input("\n\nHaжмитe Enter. чтобы выйти.")