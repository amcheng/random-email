import csv
from datetime import datetime


def log_completed_task(task, filename):
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        date_time_obj = datetime.now()
        task_info = [task, date_time_obj.replace(microsecond=0)]
        writer.writerow(task_info)


def add_task_to_completed(task, filename):
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([task])


flatten = lambda t: [item for sublist in t for item in sublist]


def csv_to_set(file_name):
    with open(file_name) as csv_file:
         reader = csv.reader(csv_file)
         return set(flatten(reader))
