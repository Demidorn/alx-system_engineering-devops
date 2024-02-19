#!/usr/bin/python3
"""
Fetch employee data from API
"""


import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_response = requests.get(f"{api_url}/users/{employee_id}")
    req = user_response.json().get('name')
    todos_response = requests.get(
            f"{api_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()
    todos_complete = []

    for todo in todos:
        if todo.get("completed") is True:
            todos_complete.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        req, len(todos_complete), len(todos)))

    for complete in todos_complete:
        print("\t {}".format(complete))
