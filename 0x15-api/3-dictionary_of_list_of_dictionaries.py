#!/usr/bin/python3
"""
Fetch employee data from API and export in JSON format
"""


import requests
import sys
import json


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    all_users_response = requests.get(f"{api_url}/users")
    all_users = all_users_response.json()

    all_tasks = {}

    for user in all_users:
        employee_id = str(user['id'])
        username = user['username']

        todos_response = requests.get(f"{api_url}/todos", params={"userId": employee_id})
        todos = todos_response.json()
        user_tasks = [
                {
                    "username": username,
                    "tasks": todo["title"],
                    "completed": todo["completed"]
                    }
                for todo in todos
                ]
        all_tasks[employee_id] = user_tasks
    with open('todo_all_employee.json', 'w') as json_file_2:
        json.dump(all_tasks, json_file_2)

