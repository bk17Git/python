import csv

with open("phonebook.csv", "a") as file:
    name = input("Enter your name: ")
    number = input("Enter you number: ")

    writer = csv.writer(file)

    writer.writerow([name, number])

