#!/usr/bin/python3
"""
Python script that exports data in the CSV format
"""


import requests
import sys
import csv


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    user_response = requests.get(f"{api_url}/users/{employee_id}")
    req = user_response.json().get('name')
    todos_response = requests.get(
            f"{api_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()
    total_task = len(todos)

    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])
        todos_complete = [task for task in todos if task["completed"]]
        completed_task = len(todos_complete)
        """csvfile.write("Employee {} is done with tasks({}/{}):".format(
            req, completed_task, total_task))"""

        for task in todos_complete:
            row = [employee_id, req, str(task["completed"]), task["title"]]
            csv_writer.writerow(row)
            """csvfile.write("\t {}".format(task.get("title")))"""
