from faker import Faker
from datetime import date
import csv

fake = Faker()

with open('names.csv', mode='w') as csvfile:
    fieldnames = ['first name', 'last name', 'date of birth']
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(3):
        writer.writerow({'first name': fake.first_name(),
                         'last name': fake.last_name(),
                         'date of birth': fake.date_of_birth()})
