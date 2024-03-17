#!/usr/bin/python3

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Export tasks for the employee with the given ID to a CSV file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user information
    user_response = requests.get(f'{base_url}/users/{employee_id}')
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
                            "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            csv_writer.writerow([employee_id, employee_name,
                                str(todo.get('completed', False)),
                                todo.get('title', '')])

    print(f"Task data exported to '{filename}' successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
