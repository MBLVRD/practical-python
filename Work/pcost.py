# pcost.py
#
# Exercise 1.27 + 1.30 + 1.31 + 1.32
import fileparse
import sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open (filename, 'rt') as f:
        portfolio = fileparse.parse_csv(f, types = [str, int, float])
        for row in portfolio:
            total_cost += row['shares'] * row['price']
    return total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} ' 'costfile')
    print('Total cost:', portfolio_cost(args[1]))

if __name__ == '__main__':
    sys.argv = ['pcost.py', 'Data\portfolio.csv']
    main(sys.argv)    