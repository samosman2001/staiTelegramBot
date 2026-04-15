import os
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
load_dotenv()

SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = int(os.getenv('SMTP_PORT',587))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
SUPPORT_EMAIL  = os.getenv('SUPPORT_EMAIL')
def send_support_email(user_id : int,username : str,user_message : str)->None:
    msg = EmailMessage()
    msg["subject"] = "Support Email"
    msg["from"] = SMTP_USER
    msg["to"] = SUPPORT_EMAIL
    msg.set_content(
        f"New message from Telegram Bot\n\n"
        f"User ID :{user_id}\n"
        f"Username :{username}\n"
        f"User Message : {user_message}\n"
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER,SMTP_PASSWORD)
        server.send_message(msg)


