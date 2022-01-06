from flask_mail import Message
from main import mail
import os


def send_message(sender_name: str, sender_email: str, body: str):
    our_email = os.environ.get("MAIL_USERNAME")
    print(f"OUR EMAIL: {our_email}")
    print(f"PASSWORD: {os.environ.get('MAIL_PASSWORD')}")
    recipients = os.environ.get("MAIL_RECIPIENTS").split(",")
    message = Message(
        subject=f"InfoPow: Message from {sender_email} / {sender_name}",
        sender=our_email,
        recipients=[our_email],
        cc=recipients,
        reply_to=sender_email,
        body=f"""
{body}
---
Message from {sender_email}
        """
    )
    mail.send(message)
