#!/usr/bin/python3
"""
Script to fetch data from an API about an employee's TODO list progress
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress
    of the employee with the given ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    try:
        # Fetching employee's todos
        response = requests.get(url)
        response.raise_for_status()
        todos = response.json()

        # Fetching employee's information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_info = user_response.json()
        employee_name = user_info.get('name')

        if not todos:
            print(f"No data found for employee ID: {employee_id}")
            return

        # Writing to CSV
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                          'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            # Writing tasks to CSV
            for todo in todos:
                writer.writerow({
                    'USER_ID': employee_id,
                    'USERNAME': employee_name,
                    'TASK_COMPLETED_STATUS': str(todo['completed']),
                    'TASK_TITLE': todo['title']
                })

        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
