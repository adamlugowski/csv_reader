from faker import Faker
import csv


def make_fake_data(number_of_rows: int):
    """
    This function is responsible to create fake data.
    :param number_of_rows: Number of rows
    :return: CSV file
    """
    fake = Faker()
    with open('names.csv', mode='w', newline='') as csvfile:
        fieldnames = ['first name', 'last name', 'date of birth']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(number_of_rows):
            writer.writerow({'first name': fake.first_name(),
                             'last name': fake.last_name(),
                             'date of birth': fake.date_of_birth()})


make_fake_data(100)
