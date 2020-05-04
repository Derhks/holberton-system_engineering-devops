#!/usr/bin/python3
"""
this script uses a REST API to query by employee ID the tasks completed
"""

if __name__ == "__main__":
    import requests
    import sys

    employed_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'
    url_name = '{:s}{:s}'.format(url, employed_id)
    request_name = requests.get('{:s}'.format(url_name))
    request_todos = requests.get('{:s}{:s}/todos/'.
                                 format(url, employed_id))
    EMPLOYEE_NAME = request_name.json().get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(request_todos.json())
    TASK_TITLE = ""
    for cnt in range(len(request_todos.json())):
        if request_todos.json()[cnt]['completed'] is True:
            NUMBER_OF_DONE_TASKS += 1
    print("Employee {:s} is done with tasks({:d}/{:d}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for cnt in range(len(request_todos.json())):
        if request_todos.json()[cnt]['completed'] is True:
            TASK_TITLE = request_todos.json()[cnt]['title']
            print("\t{:s}".format(TASK_TITLE))
