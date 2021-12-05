import csv

csv_file   = open('data.tsv', 'r')
csv_reader = csv.reader(csv_file, delimiter="\t")

header = next(csv_reader)

for record in csv_reader:

    print('Record:')

    i = 0
    for rec_value in record:
        print('  ' + header[i] + ': ' + rec_value)
        i += 1
