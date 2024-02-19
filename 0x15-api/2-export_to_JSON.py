#!/usr/bin/python3
"""
Fetch employee data from API and export in JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_response = requests.get(f"{api_url}/users/{}".format(employee_id))
    req = user_response.json().get('username')
    todos_response = requests.get(
            f"{api_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()
    user_data = {}
    user_data[employee_id] = []

    for tasks in todos:
        t = {}
        t['username'] = username
        t['task'] = tasks.get('title')
        t['completed'] = tasks.get('completed')
        user_data[employee_id].append(t)

    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(user_data, json_file)
