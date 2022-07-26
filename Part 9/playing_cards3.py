# Карты 3.0 
# Демонстрирует наследование в части переопределения методов 
class Card(object): 
    """Одна игральная карта.""" 
    RANKS = ["А" , "2", "3", "4", "5" , "6", "7", "8", "9", "10", "J", "Q", "К"] 
    SUIТS = [ "с" , "d " , "h" , "s "] 
    def init (self, rank, suit): 
        self.rank = rank 
        self.suit = suit 
    def __str__(self):
        rep = self.rank + self.suit 
        return rep
class Unprintable_Card(Card):
    """ Карта. номинал и масть которой не могут быть выведены на экран. """ 
    def __str__(self): 
        return "<нельзя напечатать>" 
class Positiоnаblе_Саrd(Card): 
    """ Карта, которую можно положить nицом или рубашкой вверх."""
    def init (self, rank, suit, face_up = True): 
        super(Positiоnаblе_Саrd.self).__init__(rank, suit) 
        self.is_face_up = face_up 