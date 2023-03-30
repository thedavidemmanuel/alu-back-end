#!/usr/bin/python3
"""
Gather data from an API and return the employee's todo list progress
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                           len(completed_tasks),
                                                           total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

