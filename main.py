from fastapi import FastAPI
from mailer import email

app = FastAPI()


@app.get("/")
async def root(
    type: str = "test",
    recipient: str = "support@accuguide.org",
    link: str = "https://accuguide.org",
):
    email(type, recipient, link)
    return {"status": "email sent successfully"}
