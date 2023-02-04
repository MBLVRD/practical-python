from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def shares(self) -> float:
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self) -> float:
        return self.shares * self.price
    
    def sell(self, num):
        self.shares -= num

    def __repr__(self) -> str:
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'


class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
        
    def cost(self):
        return 1.25 * self.shares * self.price

class NewStock(Stock):
    def yow(self):
        print('Yow!')