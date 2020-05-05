#!/usr/bin/python3
"""
this script uses a REST API to query by employee ID the tasks completed
and export data in the JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users/'
    dict_all_task = {}
    dict_task = {}

    for cnt in range(1, len(requests.get(url).json()) + 1):
        request_todos = requests.get('{:s}{:d}/todos/'.
                                     format(url, cnt))
        USER_ID = request_todos.json()[0]['userId']
        USERNAME = requests.get('{:s}{:d}'.
                                format(url, cnt)).json().get('username')
        list_task_user = []
        dict_all_task["{:d}".format(USER_ID)] = list_task_user
        for cnt in range(len(request_todos.json())):
            TASK_COMPLETED_STATUS = request_todos.json()[cnt]['completed']
            TASK_TITLE = request_todos.json()[cnt]['title']
            dict_task["task"] = TASK_TITLE
            dict_task["completed"] = TASK_COMPLETED_STATUS
            dict_task["username"] = USERNAME
            list_task_user.append(dict_task.copy())

        dict_all_task["{:d}".format(USER_ID)] = list_task_user

    with open('todo_all_employees.json', 'a') as JSON:
        json.dump(dict_all_task, JSON)
