from decimal import Decimal
""" An Employee who gets paid commission based on gross sales."""

class CommissionEmployee:
    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales
    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')
        self._gross_sales = sales

    @property
    def commission_rate(self):
        return self._commission_rate
    @commission_rate.setter
    def commission_rate(self, rate):
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError(
                'Interest rate must be greater than 0 and less than 1'
            )
        self._commission_rate = rate

    def earnings(self):
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        return (
            'Commision Employee: ' +
            f'{self.first_name} {self.last_name}\n' +
            f'Social Security Number: {self.ssn}\n' +
            f'Gross Sales: {self.gross_sales:.2f}\n' +
            f'Commission Rate: {self.commission_rate:.2f}\n' 
        )
        