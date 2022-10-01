import csv


def remove_tags(line):
    corrected_line = ''
    remove_flag = False
    for symbol in line:
        if symbol == '<':
            remove_flag = True
            continue
        if symbol == '>':
            remove_flag = False
            continue
        if not remove_flag:
            corrected_line += symbol
    return ' '.join(corrected_line.split())


def organize_some_shit(headers, line):
    dictionary = dict.fromkeys(headers, '')
    for index in range(len(headers)):
        corrected_line = remove_tags(line[index].replace('\n', ', ').strip())
        dictionary[headers[index]] = corrected_line
    return dictionary


with open(input(), 'r', encoding='utf_8_sig') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    headers = reader.__next__()
    data = []
    for row in reader:
        if '' not in row and len(row) == len(headers):
            data += [organize_some_shit(headers, row)]

for dictionary in data:
    pairs = dictionary.items()
    for name, description in pairs:
        print(name, ': ', description, sep='')
    print()
