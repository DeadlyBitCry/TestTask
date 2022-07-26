# Карты 
# Демонстрирует сочетание объектов 
class Card(object): 
    """ Одна игральная карта. """ 
    RANKS = ["А", "2", "З", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "К"] 
    SUIТS = ["с", "d", "h", "s"] 
    def __init__(self, rank, suit): 
        self.rank = rank 
        self.suit = suit 
    def __str__(self):
        rep = self.rank + self.suit 
        return rep
class Hand(object): 
    """ 'Рука': набор карт на руках у одного игрока. """ 
    def __init__(self): 
        self.cards = [] 
    def __str__(self): 
        if self.cards:
            rep = "" 
            for card in self.cards:
                rep += str(card) + "  " 
        else: 
            rep = "<nусто>" 
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
# основная часть
cardl = Card(rank = "A", suit ="с")
print("Bывoжy на экран объект-карту:")
print(cardl)
card2 = Card(rank = "2", suit ="с")
cardЗ = Card(rank = "З", suit ="с")
card4 = Card(rank = "4", suit ="с")
card5 = Card(rank = "5", suit ="с")
print("\nBывoжy еще четыре карты:")
print(card2)
print(cardЗ)
print(card4)
print(card5)
my_hand = Hand()
print("\nПeчaтaю карты, которые у меня на руках до раздачи:")
print(my_hand)
my_hand.add(cardl)
my_hand.add(card2)
my_hand.add(cardЗ)
my_hand.add(card4)
my_hand.add(card5)
print("\nПeчaтaю пять карт. которые появились у меня на руках:")
print(my_hand)
your_hand = Hand()
my_hand.give(cardl, your_hand)
my_hand.give(card2, your_hand)
print("\nПepвыe две из моих карт я передал вам.")
print("Теперь у вас на руках:")
print(your_hand)
print("A у меня на руках:")
print(my_hand)
my_hand.clear()
print("\nУ меня на руках после того. как я сбросил все карты:")
print(my_hand)
input("\n\nHaжмитe Enter, чтобы выйти.")