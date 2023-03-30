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
    request_employees = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    """
        convert json to list of dictionaries
    """
    employees = json.loads(request_employees.text)

    """
        dictionary to store all tasks for all employees
    """
    all_tasks = {}

    """
        loop through all employees
    """
    for employee in employees:
        """
            request user's TODO list
        """
        request_todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee['id']))
        """
            convert json to list of dictionaries
        """
        employee_todos = json.loads(request_todos.text)

        """
            list of dictionaries to store tasks for current employee
        """
        tasks = []

        """
            loop through dictionary & get completed tasks
        """
        for dictionary in employee_todos:
            task = {
                "username": employee['username'],
                "task": dictionary.get("title"),
                "completed": dictionary.get("completed")
            }
            tasks.append(task)

        all_tasks[employee['id']] = tasks

    """
        export to JSON
    """
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(all_tasks, file)
