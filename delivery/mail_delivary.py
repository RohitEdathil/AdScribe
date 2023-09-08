from delivery.delivery import Delivery
from models.user import User
import smtplib, ssl
from dotenv import load_dotenv
from os import environ

load_dotenv()

class MailDelivary(Delivery):
    def __init__(self): 
        self.port = 465
        self.password = environ["USER_PASSWORD"]
    def deliver(self, user: User, content: str) -> None:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login("sivanandus2003@gmail.com", self.password)
            server.sendmail("sivanandus2003@gmail.com", user.email, content)
