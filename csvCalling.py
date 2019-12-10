import csv

with open('/home/qainfotech/Downloads/dwelling.csv' , 'r') as f:
    reader = csv.reader(f)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'{" - ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} - {row[1]} - {row[2]}')
            line_count += 1

