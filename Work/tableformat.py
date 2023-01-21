class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()
	
    def row(self, rowdata):
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') *len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr><th>', end = '')
        print('</th><th>'.join(headers), end = '')
        print('</th></tr>')

    def row(self, rowdata):
        print('<tr><td>', end = '')
        print('</td><td>'.join(rowdata), end = '')
        print('</td></tr>')

def create_formatter(format):
        if format == 'txt':
            formatter = TextTableFormatter()
        elif format == 'csv':
            formatter = CSVTableFormatter()
        elif format == 'html':
            formatter = HTMLTableFormatter()
        else:
            raise RuntimeError(f'Unknown format {format}')
        return formatter

def print_table(portfolio, columns, formatter):
    formatter.headings(columns)
    for e in portfolio:
        result = ([str(getattr(e, colname)) for colname in columns])
        formatter.row(result)