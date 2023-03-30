#!/usr/bin/python3
"""
    python script that exports data in the CSV, JSON format
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    """
        convert json to dictionary
    """
    user = json.loads(request_employee.text)
    """
        extract username
    """
    username = user.get("username")

    """
        request user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status(completed) in boolean format
    """
    tasks = {}
    """
        convert json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    """
        loop through dictionary & get completed tasks
    """
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        export to CSV
    """
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([argv[1], username, v, k])

    """
        export to JSON for single user
    """
    user_dict = {}
    user_dict[argv[1]] = [{"task": k, "completed": v, "username": username} for k, v in tasks.items()]
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(user_dict, file)

    """
        export to JSON for all users
    """
    request_all_employees_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    all_todos = json.loads(request_all_employees_todos.text)
    all_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    todo_all_employees_dict = {}
    for user in all_users:
        user_tasks = [task for task in all_todos if task['userId'] == user['id']]
        todo_all_employees_dict[user['id']] = [{"task": task['title'], "completed": task['completed'], "username": user['username']} for task in user_tasks]
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todo_all_employees_dict, file)
