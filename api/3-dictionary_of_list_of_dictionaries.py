#!/usr/bin/python3
"""
    python script that exports data in the CSV and JSON format
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        request user info by employee ID
    """
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    """
        export to CSV
    """
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        for todo in todos:
            if str(todo.get('userId')) == str(argv[1]):
                username = next((user.get('username') for user in users
                                  if user.get('id') == todo.get('userId')), None)
                file_editor.writerow([argv[1], username, todo.get('completed'), todo.get('title')])

    """
        export to JSON
    """
    output_dict = {}
    for todo in todos:
        user_id = todo.get('userId')
        username = next((user.get('username') for user in users if user.get('id') == user_id), None)
        if user_id not in output_dict:
            output_dict[user_id] = []
        output_dict[user_id].append({"username": username, "task": todo.get('title'),
                                     "completed": todo.get('completed')})

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(output_dict, file)
