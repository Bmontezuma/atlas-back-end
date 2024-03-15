#!/usr/bin/python3
"""
This script retrieves information about a user's TODO list progress
from a REST API based on the provided employee ID and exports
it to JSON format.
"""

import json
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

    # Construct JSON data
    json_data = {str(employee_id): [{"task": todo['title'], "completed":
                 todo['completed'], "username": employee_name}
                 for todo in todos_data]}

    # Write data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)
    print(f"Task data exported to '{filename}' successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
