from time1 import Account, Time
from decimal import Decimal

account1 = Account('John Snow', Decimal('50.00'))
account1.balance = Decimal('-1000.00')

t1 = Time(23,45,55)
t1.set_time(13,55,55)
print(t1)