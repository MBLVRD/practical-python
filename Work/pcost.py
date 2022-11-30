# pcost.py
#
# Exercise 1.27 + 1.30 + 1.31 + 1.32
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rownum, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rownum}: Bad row: {row}')
        return total_cost
    
cost = portfolio_cost('Data/portfoliodate.csv')
print('Total cost:', cost)