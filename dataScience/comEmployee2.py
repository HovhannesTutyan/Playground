from comEmployee import CommissionEmployee
from decimal import Decimal

c = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
print(f'{c.earnings():,.2f}')
c.gross_sales = Decimal('20000')
print(f'{c.earnings():,.2f}')
