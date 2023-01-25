# pcost.py
#
# Exercise 1.27 + 1.30 + 1.31 + 1.32
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum([e.cost for e in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} ' 'costfile')
    print('Total cost:', portfolio_cost(args[1]))

if __name__ == '__main__':
    main(['pcost.py', 'Data\portfolio.csv'])    