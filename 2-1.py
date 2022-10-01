import csv

with open(input(), 'r', encoding='utf_8_sig') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    headers = reader.__next__()
    data = []
    for row in reader:
    	if '' not in row and len(row) == len(headers):
        	data += [row]

print(headers)
print(data)
