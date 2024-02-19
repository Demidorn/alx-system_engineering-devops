#!/usr/bin/python3
"""
Fetch employee data from API and export in JSON format
"""

import requests
import sys
import json

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_response = requests.get(f"{api_url}/users/{employee_id}")
    req = user_response.json().get('name')
    todos_response = requests.get(
            f"{api_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    user_data = {
        employee_id: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": req
            }
            for todo in todos
        ]
    }

    with open(f"{employee_id}.json", 'w') as json_file:
        json.dump(user_data, json_file)
