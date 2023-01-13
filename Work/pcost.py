# pcost.py
#
# Exercise 1.27 + 1.30 + 1.31 + 1.32
import fileparse

def portfolio_cost(filename):
    total_cost = 0.0
    portfolio = fileparse.parse_csv(filename, types = [str, int, float])
    for row in portfolio:
        total_cost += row['shares'] * row['price']
    return total_cost
    
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)