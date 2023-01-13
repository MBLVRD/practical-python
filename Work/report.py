# report.py
# Exercise 2.16
import fileparse
from collections import Counter

def read_portfolio(filename):

    return fileparse.parse_csv(filename)

def read_prices(filename):

    return dict(fileparse.parse_csv(filename, has_headers = False, types = [str, float]))

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

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
report_formatted_out(report)