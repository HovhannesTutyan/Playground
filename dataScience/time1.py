from decimal import Decimal
<<<<<<< HEAD

class Account:
    def __init__(self, name, balance):
        if (balance < Decimal('0.00')):
            raise ValueError('Initial balance can not be negative')
        self.name    = name
        self.balance = balance
    
    def deposit(self, amount):
        if (amount < Decimal('0.00')):
            raise ValueError("Amount can not be negative")
=======
import random

class Account:
    def __init__(self, name, balance):
        if(balance < Decimal("0.00")):
            raise ValueError(f'Balance {balance} can not be negative ')
        self.name    = name
        self.balance = balance

    def deposit(self, amount):
        if (amount < Decimal("0.00")):
            raise ValueError(f'Amount {amount} can not be negative')
>>>>>>> 64e17d3f11debb8870b401be21810b467f9c68db
        self.balance += amount
    
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour   = hour
        self.minute = minute
        self.second = second
    
    @property
    def hour(self):
<<<<<<< HEAD
        return self._hour
    @hour.setter
    def hour(self, hour):
        if not(0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        self._hour = hour
    
    @property
    def minute(self):
        return self._minute
    @minute.setter
    def minute(self, minute):
        if not(0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-60')
        self._minute = minute

    @property
    def second(self):
        return self._second
    @second.setter
    def second(self, second):
        if not(0 <= second < 60):
            raise ValueError(f'Second {second} must be 0-60')
        self._second = second
    
    def set_time(self, hour=0, minute=0, sec=0):
        self.hour   = hour
        self.minute = minute
        self.second = sec

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, second={self.second})')
    
    def __str__(self):
        return (('12' if self.hour in (0,12) else str(self.hour % 12)) + f':{self.minute:0>2}:{self.second:0>2}' + ('AM' if self.hour < 12 else 'PM'))
=======
        return self.__hour
    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour {hour} must be 0-23')
        self.__hour = hour
    
    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f'The {minute} minute must be 0-59')
        self.__minute = minute

    @property
    def second(self):
        return self.__second
    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f'The {second} minute must be 0-59')
        self.__second = second
    
    def set_time(self, hour=0, minute=0, second=0):
        self.hour   = hour
        self.minute = minute
        self.second = second
    
    def __repr__(self) -> str:
        return (f'Time (hour={self.hour}, minute={self.minute}, second={self.second})')
    def __str__(self) -> str:
        return ('12' if self.hour in (0,12) else str(self.hour % 12) + f':{self.minute:0>2}:{self.second:0>2}' + ("AM" if self.hour < 12 else "PM"))

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    def __init__(self, face, suit) -> None:
        self._face = face
        self._suit = suit
    
    @property
    def face(self):
        return self._face
    @property
    def suit(self):
        return self._suit
    @property
    def image_name(self):
        return str(self).replace('', '-') + '.png'

    def __repr__(self) -> str:
        return (f'Card(face = {self.face}, suit = {self.suit})')
    def __str__(self) -> str:
        return (f'{self.face} of {self.suit}')
    def __format__(self, format: str) -> str:
        return (f'{str(self):{format}}')
        
class DeckOfCards:
    NUMBER_OF_CARDS = 52

    def __init__(self) -> None:
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], Card.SUITS[count // 13]))

    def shuffle(self):
        self._current_card = 0
        random.shuffle(self._deck)
    
    def deal_card(self):
        try:
            card = self._deck[self._current_card]  
            self._current_card += 1
            return card
        except:
            return None
    
    def __str__(self) -> str:
        s = ''
        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        return s
>>>>>>> 64e17d3f11debb8870b401be21810b467f9c68db
