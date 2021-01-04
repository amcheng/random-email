import tasks
import email_functions
import files

todays_task = tasks.get_random_task()
email_functions.send_email(todays_task)
tasks.update_completed_tasks(todays_task)