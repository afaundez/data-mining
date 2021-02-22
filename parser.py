import re

columns = {}

with open('metadata.txt') as f:
    column = None
    for line in f:
        if re.match('[^\s]+\:\s.*$', line):
            column, column_description = line.rstrip().split(': ')
            columns[column] = { 'description': column_description }
        elif re.match('^\s+.*\t.*$', line):
            value, value_description = line.strip().split('\t')
            if not 'values' in columns[column].keys():
                columns[column]['values'] =  {}
            columns[column]['values'][value] = value_description
            print(f'---{value}---{value_description}---')
print(columns)
