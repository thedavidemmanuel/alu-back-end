#!/usr/bin/python3
"""
    Python script that returns TODO list progress for a given employee ID
    and exports the data to a CSV file.
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    # Request employee info by employee ID
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")

    # Request user's TODO list
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    employee_todos = json.loads(request_todos.text)

    # Export data to a CSV file
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for todo in employee_todos:
            csv_writer.writerow([argv[1], employee_name, todo['completed'], todo['title']])

    print("Data exported to {}.csv".format(argv[1]))

