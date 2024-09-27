# fileparse.py
# Exercise 3.3 -> 3.14
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    rows = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else []
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    records = []
    for num_of_row, row in enumerate(rows, 1):
        try:
            if not row:
                continue
            if select:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print('Row ', num_of_row, ': Couldn\'t convert', row)
                print('Row ', num_of_row, ':', e)
    return records