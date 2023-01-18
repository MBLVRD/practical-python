# report.py
# Exercise 2.16
import fileparse
import sys
import stock

def read_portfolio(filename):
    with open(filename, 'rt') as lines:
        portfolio = fileparse.parse_csv(lines, select = ['name', 'shares', 'price'], types = [str, int, float])
        return [stock.Stock(element['name'], element['shares'], element['price']) for element in portfolio]

def read_prices(filename):
    with open(filename, 'rt') as f:
        return dict(fileparse.parse_csv(f, has_headers = False, types = [str, float]))

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
        name = temp.name
        shares = temp.shares
        price = prices[temp.name]
        change = price - temp.price
        cur_tuple = (name, shares, price, change)
        result.append(cur_tuple)
    return result

def main (args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfolio = read_portfolio(args[1])
    prices = read_prices(args[2])
    report = make_report(portfolio, prices)
    report_formatted_out(report)

if __name__ == '__main__':
    sys.argv = ['report.py', 'Data\portfolio.csv', 'Data\prices.csv']
    main(sys.argv)    