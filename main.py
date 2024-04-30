import csv
from datetime import datetime


def get_person_details():
    """
    This function is responsible for reading csv file.
    :return: Personal info in terminal
    """
    with open('names.csv', mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        today = datetime.today()
        for row in reader:
            date_of_birth = datetime.strptime(row['date of birth'], '%Y-%m-%d')
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            print('Name:', row['first name'], '\n''Last name:', row['last name'], '\n''Age:', age, '\n')


get_person_details()
