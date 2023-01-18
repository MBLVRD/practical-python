class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, num):
        self.shares -= num

a = Stock('Google', 100, 94.4)
a.sell(13)
print (a.cost())