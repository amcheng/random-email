import os

CURRENT_MODULE_PATH = os.path.abspath(__file__)
CURRENT_MODULE_DIRECTORY = os.path.dirname(CURRENT_MODULE_PATH)

ALL_TASKS_CSV_FILENAME = 'all_tasks.csv'
TEST_TASKS_CSV_FILENAME = 'test_tasks.csv'
COMPLETED_TASKS_CSV_FILENAME = 'completed_tasks.csv'
LOG_COMPLETED_TASKS_CSV_FILENAME = 'completed_tasks_log.csv'
EMAIL_PASSWORD_FILENAME = 'email_info.txt'

ALL_TASKS_CSV_FILE_PATH = os.path.join(CURRENT_MODULE_DIRECTORY, ALL_TASKS_CSV_FILENAME)
TEST_TASKS_CSV_FILE_PATH = os.path.join(CURRENT_MODULE_DIRECTORY, TEST_TASKS_CSV_FILENAME)
COMPLETED_TASKS_CSV_FILE_PATH = os.path.join(CURRENT_MODULE_DIRECTORY, COMPLETED_TASKS_CSV_FILENAME)
LOG_COMPLETED_TASKS_CSV_FILE_PATH = os.path.join(CURRENT_MODULE_DIRECTORY, LOG_COMPLETED_TASKS_CSV_FILENAME)
EMAIL_PASSWORD_FILE_PATH = os.path.join(CURRENT_MODULE_DIRECTORY, EMAIL_PASSWORD_FILENAME)