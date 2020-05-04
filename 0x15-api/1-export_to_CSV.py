#!/usr/bin/python3
"""
this script uses a REST API to query by employee ID the tasks completed
and export data in the CSV format
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
    for cnt in range(len(request_todos.json())):
        USER_ID = request_todos.json()[cnt]['userId']
        TASK_COMPLETED_STATUS = request_todos.json()[cnt]['completed']
        TASK_TITLE = request_todos.json()[cnt]['title']
        with open('USER_ID.csv', 'a') as CSV:
            CSV.write('"{:d}", "{:s}", "{}", "{:s}"\n'.
                      format(USER_ID, USERNAME,
                             TASK_COMPLETED_STATUS, TASK_TITLE))
