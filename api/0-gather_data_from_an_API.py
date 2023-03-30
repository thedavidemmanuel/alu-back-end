#!/usr/bin/python3
"""
    Python script that returns TODO list progress for a given employee ID
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        Request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        Convert JSON to dictionary
    """
    employee = json.loads(request_employee.text)
    """
        Extract employee name
    """
    employee_name = employee.get("name")

    """
        Request user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        Dictionary to store task status in boolean format
    """
    tasks = {}
    """
        Convert JSON to list of dictionaries
    """
    employee_todos = json.loads(request_todos.text)
    """
        Loop through dictionary and get completed tasks
    """
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        Return name, total number of tasks and completed tasks
    """
    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))
