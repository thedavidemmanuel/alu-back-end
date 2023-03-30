#!/usr/bin/python3
"""
    python script that exports data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
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
        list to store task status(completed) in dictionary format
    """
    tasks = []
    """
        convert json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    """
        loop through dictionary & get completed tasks
    """
    for dictionary in user_todos:
        task = {}
        task["task"] = dictionary.get("title")
        task["completed"] = dictionary.get("completed")
        task["username"] = username
        tasks.append(task)

    """
        export to JSON
    """
    with open('{}.json'.format(argv[1]), 'w') as json_file:
        json.dump({argv[1]: tasks}, json_file)
