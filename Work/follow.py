# follow.py
import os, time, csv

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line

def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('Work\Data\portfolio.csv')
    lines = follow('Work\Data\stocklog.csv')
    rows = csv.reader(lines)
    for row in rows:
        print(row)

    '''
    for line in follow('Work\Data\stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
            '''