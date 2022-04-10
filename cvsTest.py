import csv

with open('test.csv', 'w') as justcsv:
    heading = ['name', 'age']

    csv_writer = csv.DictWriter(justcsv, fieldnames=heading)
    
    csv_writer.writeheader()

    # csv_writer.writerow([('name','1'), ('age', '2')])