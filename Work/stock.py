class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
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