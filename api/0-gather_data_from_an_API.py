#!/usr/bin/python3
"""
a Python script that, using this REST API,
https://jsonplaceholder.typicode.com/path/?query#fragments
for a given employee ID, returns information about his/her
TODO list progress.

Requirements:
use urllib or requests module
The script must accept an integer as a parameter,
which is the employee ID
The script must display on the standard output the
employee TODO list progress in this exact format:

First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is
the sum of completed and non-completed tasks

Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    """
    format the employees id with the url
    https://jsonplaceholder.typicode.com/users/{employees_id}
    after getting it from the command line using the sys module
    """
    import requests

def get_emp_todo(emp_id):
    TODO_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    USER_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}"

    # Get the JSON of TODOS - DONE
    # Get TOTAL NUMBER of todos - DONE
    # Get COMPLETED NUMBER of todos - DONE
    # Get THE NAME of the employee - DONE 

    # GET THE TITLES OF THE COMPLETED TASKS
    completed_tasks = []
    # AND PRINT THEM ALL OUT ON STDOUT
    for task in response1:
	if task [‘completed’] is not True:
		continue
 	completed_tasks.append (task)
    # EACH TASKS SHOULD BE PRINTED ON A NEW LINE
    no_of_completed_tasks = len(completed_tasks)
    total_no_of_tasks = len(response1)

    emp_name = requests.get(USER_URL).json()["name"]
    emp_todos = requests.get(TODO_URL).json()
    emp_total_todos = len(emp_todos)
    emp_completed_todos = 0
    for todo in emp_todos:
        if todo["completed"] is True:
            emp_completed_todos += 1
    print(f"Employee {emp_name} From total todos of {emp_total_todos}, {emp_completed_todos} tasks have been done")


get_emp_todo(3)

