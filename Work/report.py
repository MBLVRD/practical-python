# report.py
# Exercise 2.16
import fileparse, stock, tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    with open(filename) as lines:
        portfolio = fileparse.parse_csv(lines, 
                                        select = ['name', 'shares', 'price'], 
                                        types = [str, int, float], 
                                        **opts)
        result = [stock.Stock(**element) for element in portfolio]
        return Portfolio(result)

def read_prices(filename):
    with open(filename, 'rt') as f:
        return dict(fileparse.parse_csv(f, has_headers = False, types = [str, float]))

def print_report(report_data, formatter):
    for e in report_data:
        rowdata = [e['name'], str(e['shares']), f'{e["price"]:0.2f}', f'{e["change"]:0.2f}']
        formatter.row(rowdata)

def make_report_data(portfolio, prices):
    result = []
    for line in portfolio:
        cur_dict = {'name': line.name, 
                    'shares': line.shares, 
                    'price': prices[line.name], 
                    'change': prices[line.name] - line.price}
        result.append(cur_dict)
    return result

def portfolio_report(portfolio_file, price_file, format):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)
    report = make_report_data(portfolio, prices)

    formatter = tableformat.create_formatter(format)
    print_report(report, formatter)
    tableformat.print_table(portfolio, ['name', 'shares'], formatter)

def main (args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    main(['report.py', 'Work\Data\portfolio.csv', 'Work\Data\prices.csv', 'txt'])  