import csv_functions
import random
import files

def get_random_task():
    all_tasks = csv_functions.csv_to_set(files.ALL_TASKS_CSV_FILE_PATH)
    completed_tasks = csv_functions.csv_to_set(files.COMPLETED_TASKS_CSV_FILE_PATH)

    uncompleted_tasks = all_tasks.difference(completed_tasks)

    if not uncompleted_tasks:
        return ""

    # print(uncompleted_tasks)
    task = random.choice(list(uncompleted_tasks))
    return task

def update_completed_tasks(task):
    if not task:
        return
    csv_functions.add_task_to_completed(task, files.COMPLETED_TASKS_CSV_FILE_PATH)
    csv_functions.log_completed_task(task, files.LOG_COMPLETED_TASKS_CSV_FILE_PATH)