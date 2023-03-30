#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    user_id = argv[1]

    # Get user info
    response = requests.get(url + user_id)
    user_info = response.json()
    employee_name = user_info.get('name')

    # Get tasks
    response = requests.get(url + user_id + "/todos")
    tasks = response.json()
    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task.get("completed")]

    # Print results
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                           len(completed_tasks),
                                                           total_tasks))
    for task in completed_tasks:
        print("\t {} {}".format('\t', task.get('title')))

