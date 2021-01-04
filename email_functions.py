from email.mime.text import MIMEText
import smtplib
import ssl
import files

SENDER_EMAIL = 'alecheng.dev@gmail.com'
SENDER_NAME = '30 Days of Random Bot'
EMAIL_SUBJECT = 'Your random challenge!'
PORT = 465  # For SSL
SMTP_SERVER = 'smtp.gmail.com'

RECIPIENT_EMAILS = ['cubesolver@gmail.com', 'dewalgupta@gmail.com', 'beauhoover1@gmail.com', 'theanuvedverma@gmail.com']
TEST_RECIPIENT_EMAILS = ['cubesolver@gmail.com']

NO_TASK_MESSAGE = 'Congratulations! You have completed 30 days of random!'

def get_password(filename):
    file = open(filename, 'r')
    return file.read()


def build_email_body(task):
    if not task:
        return NO_TASK_MESSAGE
    return f'Here is your random challenge: {task}'


def build_full_email_message(task):
    msg = MIMEText(build_email_body(task), 'html')
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = SENDER_NAME
    msg_string = msg.as_string()
    return msg_string


def send_email(task):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER_EMAIL, get_password(files.EMAIL_PASSWORD_FILE_PATH))

        email_message = build_full_email_message(task)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAILS, email_message)