#!/usr/bin/python3
"""
this script uses a REST API to query by employee ID the tasks completed
and export data in the JSON format
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    employed_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'
    url_employed = '{:s}{:s}'.format(url, employed_id)
    request_employed = requests.get('{:s}'.format(url_employed))
    USERNAME = request_employed.json().get('username')
    request_todos = requests.get('{:s}{:s}/todos/'.
                                 format(url, employed_id))
    user_dict = {}
    task_list = []
    dict_task = {}
    dict_task["username"] = USERNAME
    USER_ID = request_todos.json()[0]['userId']
    for cnt in range(len(request_todos.json())):
        TASK_COMPLETED_STATUS = request_todos.json()[cnt]['completed']
        TASK_TITLE = request_todos.json()[cnt]['title']
        dict_task["task"] = TASK_TITLE
        dict_task["completed"] = TASK_COMPLETED_STATUS
        task_list.append(dict_task)
    user_dict["{:d}".format(USER_ID)] = task_list
    with open('USER_ID.json', 'a') as JSON:
        JSON.write(str(user_dict))
