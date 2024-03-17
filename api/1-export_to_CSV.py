#!/usr/bin/python3

"""
This script retrieves information about a user's TODO list progress
from a REST API based on the provided employee ID and exports it to a CSV file.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Retrieve and export information about the user's TODO list progress.

    Args:
        employee_id (int): The employee ID for which to retrieve the TODO list.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    if user_response.status_code != 200:
        print("User ID not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name', '')

    # Get user's todos
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Write data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS",
                             "TASK_TITLE"])
        for todo in todos_data:
            csv_writer.writerow([
                employee_id,
                employee_name,
                str(todo.get('completed', False)),
                todo.get('title', '')
            ])

    print(f"Task data exported to '{filename}' successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
