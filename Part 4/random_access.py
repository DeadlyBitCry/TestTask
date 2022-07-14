import random 
word = "индекс" 
print ("В переменной word хранится слово: " + word + "\n") 
high = len(word) 
low = -len(word) 
for i in range(10): 
    position = random.randrange(low , high) 
    print ( "word[" + str(position) + "]\t" + str(word[position]))