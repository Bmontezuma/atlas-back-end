#!/usr/bin/python3
import os
import sys
import requests


def get_employee_data(employee_id):
    """
    This function fetches employee data from an API.
    :param employee_id: The ID of the employee to fetch data for.
    :return: A dictionary containing employee data.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: Unable to fetch data
                        for employee ID {employee_id}.")


def main():
    """
    The main function of the script.
    """
    employee_id = 1
    employee_data = get_employee_data(employee_id)
    print(f"Employee {employee_data['name']} is done with tasks
          ({employee_data['completed_tasks']}
          / {employee_data['total_tasks']}): ")
    for task in employee_data['tasks']:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    main()
