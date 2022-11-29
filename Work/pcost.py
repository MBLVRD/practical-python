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
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except ValueError:
                print(f'Row {rownum}: Bad row: {row}')
        return total_cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)