def display(message) : 
    print(message) 
def give_me_five() : 
    five = 5 
    return five
def ask_yes_no(question) :
    response = None
    while response not in ("у", "n") : 
        response = input(question).lower() 
    return response 
display("Baм сообщение. \n") 
number = give_me_five() 
print("Boт что возвратила функция give_me_five(): " + str(number)) 
answer = ask_yes_no("\nПожалуйста, введите 'y' или 'n': ") 
print("Спасибо, что ввели " + answer) 
input("\n\nHaжмитe Enter. чтобы выйти.")