# pcost.py
#
# Exercise 1.27 + 1.30 + 1.31 + 1.32
import sys
def portfolio_cost(filename):
    import csv
    counterOfLines = 0
    Total_cost = 0.00
    try:
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for name, shares, price in rows:
                try:
                    counterOfLines += 1
                    Total_cost += int(row[1]) * float(row[2])
                except IndexError:
                    print('Проблема со строкой', counterOfLines, ': не хватает информации')
                    pass    
        return Total_cost
    except FileNotFoundError:
        print('Ну ты чего, братишка? Такого файла нет!')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)