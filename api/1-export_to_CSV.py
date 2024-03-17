#!/usr/bin/python3
"""
Script to retrieve task data from a REST API based on a given user ID,
and export it to a CSV file.
"""

import csv
import requests
import sys


def export_to_csv(user_id):
    """
    Retrieve task data for the specified user ID from a REST API and
    export it to a CSV file.

    Args:
        user_id (int): The ID of the user whose task data is to be retrieved.

    Returns:
        int: The number of tasks exported to the CSV file.
    """
    # Base URL for the REST API
    API_URL = "https://jsonplaceholder.typicode.com"

    try:
        # Make a GET request to retrieve task data for the user ID
        response = requests.get(
            f"{API_URL}/users/{user_id}/todos",
            params={"_expand": "user"}
        )

        # Check if the request was successful
        response.raise_for_status()

        # Convert JSON response to Python dictionary
        data = response.json()

        # Check if tasks were found for the user ID
        if not data:
            print("No tasks found for user ID", user_id)
            sys.exit(1)

        # Extract username from the first task
        username = data[0]["user"]["username"]

        # Write task data to a CSV file
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            task_count = 0  # Initialize task count
            for task in data:
                writer.writerow([
                    user_id,
                    username,
                    str(task["completed"]),
                    task["title"]
                ])
                task_count += 1  # Increment task count

        return task_count

    except requests.exceptions.RequestException as e:
        print(f"RequestError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {sys.argv[0]} <user_id>")
        sys.exit(1)

    # Get user ID from command-line arguments
    user_id = sys.argv[1]

    # Call the export_to_csv function with the provided user ID
    tasks_exported = export_to_csv(user_id)

    # Check if the correct number of tasks was exported
    expected_tasks = 20  # Assuming there are supposed to be 20 tasks
    if tasks_exported == expected_tasks:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")
