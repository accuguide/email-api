import smtplib, ssl
import os
from dotenv import load_dotenv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

EMAIL = os.getenv("EMAIL")
TOKEN = os.getenv("TOKEN")
SERVER = os.getenv("SERVER")
PORT = int(os.getenv("PORT"))

context = ssl.create_default_context()


def email(type, recipient, link):
    try:
        server = smtplib.SMTP(SERVER, PORT)
        server.starttls(context=context)
        server.login(EMAIL, TOKEN)
        send(server, type, recipient, link)
    except Exception as e:
        print(e)
    finally:
        server.quit()


def send(server, type, recipient, link):
    try:
        message = MIMEMultipart("alternative")
        message["From"] = EMAIL
        message["To"] = recipient
        global body
        if type == "test":
            message["Subject"] = "Accuguide Support - Test Email"
            body = f"This is a test email from Accuguide, with the link {link}"
        if type == "reset":
            message["Subject"] = "Accuguide Support - Password Reset"
            body = f"You are recieving this email because you requested a password reset. Click the link below to reset your password.\n{link}"
        closing = "\n\nWarm Regards,\nAccuguide Support\nhttps://accuguide.org"
        body += closing
        body_mime = MIMEText(body, "plain")
        message.attach(body_mime)
        server.sendmail(EMAIL, recipient, message.as_string())
    except Exception as e:
        print(e)
        return None
