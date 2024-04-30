import csv


with open('names.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print('Imię:', row['first name'], '\n'
              'Nazwisko:', row['last name'], '\n'
              'Data urodzenia:', row['date of birth'], '\n')
