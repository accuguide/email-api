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
    server = smtplib.SMTP(SERVER,PORT)
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
    message["Subject"] = "Accuguide - Test Email"
    message["From"] = EMAIL
    message["To"] = recipient
    body = f"This is a test email from Accuguide, with the link {link}"
    body_mime = MIMEText(body, "plain")
    message.attach(body_mime)
    server.sendmail(EMAIL, recipient, message.as_string())
  except Exception as e:
    print(e)
    return None
