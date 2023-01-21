# report.py
# Exercise 2.16
import fileparse, stock, tableformat

def read_portfolio(filename):
    with open(filename, 'rt') as lines:
        portfolio = fileparse.parse_csv(lines, select = ['name', 'shares', 'price'], types = [str, int, float])
        result = [stock.Stock(element['name'], element['shares'], element['price']) for element in portfolio]
        print(result)
        return result

def read_prices(filename):
    with open(filename, 'rt') as f:
        return dict(fileparse.parse_csv(f, has_headers = False, types = [str, float]))

def print_report(report_data, formatter):
    for e in report_data:
        price = e['price']
        change = e['change']
        rowdata = [e['name'], str(e['shares']), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def make_report_data(portfolio, prices):
    result = []
    for temp in portfolio:
        cur_dict = {'name': temp.name, 
                    'shares': temp.shares, 
                    'price': prices[temp.name], 
                    'change': prices[temp.name] - temp.price}
        result.append(cur_dict)
    return result

def portfolio_report(portfolio_file, price_file, format):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)
    report = make_report_data(portfolio, prices)

    formatter = tableformat.create_formatter(format)
    print_report(report, formatter)
    tableformat.print_table(portfolio, ['shares'], formatter)

def main (args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    main(['report.py', 'Data\portfolio.csv', 'Data\prices.csv', 'txt'])    