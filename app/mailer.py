import smtplib
import os
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv # type: ignore

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_mail(to: str, subject: str, body: str, attachment: list[Path]):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    for file in attachment:
        with open(file, "rb") as f:
            file_data = f.read()
            file_name = file.name
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
        print(f"Email sent to {to} successfully!")