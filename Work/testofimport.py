from fileparse import parse_csv

result = parse_csv('Data/missing.csv', types = [str, int, float], silence_errors = True)
print (result)