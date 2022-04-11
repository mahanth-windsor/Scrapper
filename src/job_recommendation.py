import os, csv

filename = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'pageLinks.csv'))
with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)