#!/usr/bin/python3
"""
Python script that exports data in the CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    user_response = requests.get(f"{api_url}/users/{employee_id}")
    req = user_response.json().get('name')
    todos_response = requests.get(
        f"{api_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    with open('{}.csv'.format(employee_id), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for task in todos:
            writer.writerow([employee_id, req, str(task.get('completed')),
                            task.get('title')])
