#!/usr/bin/python3
"""
    Python script that exports data in the CSV format
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        Request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    """
        Convert json to dictionary
    """
    user = json.loads(request_employee.text)
    """
        Extract username
    """
    username = user.get("username")

    """
        Request user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    """
        Dictionary to store task status(completed) in boolean format
    """
    tasks = {}
    """
        Convert json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    """
        Loop through dictionary & get completed tasks
    """
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        Export to CSV
    """
    with open('{}.csv'.format(argv[1]), mode='w', newline='') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([argv[1], username, v, k])

    print('Data exported to {}.csv'.format(argv[1]))
