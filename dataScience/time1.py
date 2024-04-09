from decimal import Decimal

class Account:
    def __init__(self, name, balance):
        if (balance < Decimal('0.00')):
            raise ValueError('Initial balance can not be negative')
        self.name    = name
        self.balance = balance
    
    def deposit(self, amount):
        if (amount < Decimal('0.00')):
            raise ValueError("Amount can not be negative")
        self.balance += amount
    
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour   = hour
        self.minute = minute
        self.second = second
    
    @property
    def hour(self):
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