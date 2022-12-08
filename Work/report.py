# report.py
# Exercise 2.16
import csv
from collections import Counter

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            record['shares'] = int(record['shares'])
            record['price'] = float(record['price'])
            portfolio.append(record)
    return portfolio

def read_prices(filename):
    prices_dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row
                prices_dict[name] = float(price)
            except:
                pass
    return prices_dict

def report_formatted_out(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        temp_price = '$' + f'{price:>0.2f}'
        print(f'{name:>10s} {shares:>10} {temp_price:>10s} {change:>10.2f}')

def make_report(portfolio, prices):
    result = []
    for temp in portfolio:
        name = temp['name']
        shares = temp['shares']
        price = prices[temp['name']]
        change = float(price) - float(temp['price'])
        cur_tuple = (name, shares, price, change)
        result.append(cur_tuple)
    return result


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
report_formatted_out(report)

holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']
print(holdings)