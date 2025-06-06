from fastapi import FastAPI
from mailer import email
from security import get_api_key
from fastapi import Security

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Accuguide API. Use /mail to send an email."}


@app.get("/mail")
async def root(
    api_key: str = Security(get_api_key),
    type: str = "test",
    recipient: str = "support@accuguide.org",
    link: str = "https://accuguide.org",
):
    email(type, recipient, link)
    return {"status": "email sent successfully"}
