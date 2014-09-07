import csv

csv_file   = open('data.csv', 'r')
csv_reader = csv.reader(csv_file)

header = csv_reader.next()

for record in csv_reader:
    
    print 'Record:'
    
    i = 0
    for rec_value in record:
        print '  ' + header[i] + ': ' + rec_value
        i += 1
