#!/usr/bin/python3
"""
Script to fetch and display employee TODO list progress.
"""

import sys
import requests


def get_employee_data(employee_id):
    """
    Fetch employee data from an API.

    :param employee_id: The ID of the employee to fetch data for.
    :return: A dictionary containing employee data.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Error: Unable to fetch data for employee ID {employee_id}.")


def main():
    """
    The main function of the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data = get_employee_data(employee_id)
    total_tasks = len(employee_data['todos'])
    completed_tasks = sum(
        1 for task in employee_data['todos'] if task['completed'])

    print(f"Employee {employee_data['name']} is done with tasks
          ({completed_tasks}/{total_tasks}): ")
    for task in employee_data['todos']:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    main()
