#!/usr/bin/python3
"""
This script retrieves information about a user's TODO list progress
from a REST API based on the provided employee ID.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display information about the user's TODO list progress.

    Args:
        employee_id (int): The employee ID for which to retrieve the TODO list.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data['name']

    # Get user's todos
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Count total and completed tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display progress
    print(f"Employee {employee_name} is done with tasks "
          f"({completed_tasks}/{total_tasks}):")

    # Display completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
