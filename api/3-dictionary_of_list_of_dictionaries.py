#!/usr/bin/python3
"""
This script retrieves information about TODO list progress
from a REST API based on the provided employee ID.
"""

import json
import requests


def get_all_employees_todo_progress():
    """
    Retrieve and aggregate information about tasks from all employees.

    Returns:
        dict: A dictionary of lists of dictionaries
        containing tasks for all employees.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Initialize dictionary to store all tasks
    all_tasks = {}

    # Get list of users
    users_response = requests.get(f'{base_url}/users')
    users_data = users_response.json()

    # Iterate over each user to get their tasks
    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Get user's todos
        todos_response = requests.get(f'{base_url}/todos?userId={user_id}')
        todos_data = todos_response.json()

        # Store tasks in the dictionary
        all_tasks[str(user_id)] = [
            {"username": username, "task": todo['title'],
             "completed": todo['completed']}
            for todo in todos_data
        ]

    return all_tasks


def export_all_tasks_to_json(all_tasks):
    """
    Export all tasks data to a JSON file.

    Args:
        all_tasks (dict): A dictionary of lists of dictionaries
        containing tasks for all employees.

    Returns:
        None
    """
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)
    print(f"All tasks data exported to '{filename}' successfully.")


if __name__ == "__main__":
    all_tasks = get_all_employees_todo_progress()
    export_all_tasks_to_json(all_tasks)
