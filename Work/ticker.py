# ticker.py

from follow import follow
import csv

def ticker(portfile, logfile, fmt):
    from report import read_portfolio
    import tableformat
    result = filter_symbols(parse_stock_data(follow(logfile)), read_portfolio(portfile))
    formatter = tableformat.create_formatter(fmt)
    columns = ['name', 'price', 'change']
    formatter.headings(columns)
    for e in result:
        formatter.row([str(e[colname]) for colname in columns])

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        for n, type in enumerate(types):
           row[n] = type(row[n])
        yield row

def make_dicts(rows, headers):
    return (dict(zip(headers,row)) for row in rows)

def filter_symbols(rows, names):
    rows = (row for row in rows if row['name'] in names)
    return rows

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

if __name__ == '__main__':
    ticker('Work\Data\portfolio.csv', 'Work\Data\stocklog.csv', 'txt')

