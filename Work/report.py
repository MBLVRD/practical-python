# report.py
#
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
    headers = ('Name', 'Shares', 'Date', 'Time' ,'Price', 'Change')
    print('%10s %10s %10s %10s %10s %10s' % headers)
    for e in headers:
        print('-' * 10, end =' ')
    print()
    for name, shares, date, time, price, change in report:
        temp_price = '$' + f'{price:>0.2f}'
        print(f'{name:>10s} {shares:>10} {date:>10} {time:>10} {temp_price:>10s} {change:>10.2f}')

def make_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    result = []
    for temp in portfolio:
        name = temp['name']
        shares = temp['shares']
        price = prices[temp['name']]
        change = float(price) - float(temp['price'])
        date = temp['date']
        time = temp['time']
        cur_tuple = (name, shares, date, time, price, change)
        result.append(cur_tuple)
    return result

report = make_report('Data/portfoliodate.csv', 'Data/prices.csv')
port = read_portfolio('Data/portfoliodate.csv')
report_formatted_out(report)