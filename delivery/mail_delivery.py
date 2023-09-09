from delivery.delivery import Delivery
from models.user import User
import smtplib, ssl

from os import environ


class MailDelivery(Delivery):
    """Class for mail delivery"""

    def __init__(self):
        self.port = 465
        self.password = environ["SMTP_PASSWORD"]

    def deliver(self, user: User, content: str) -> None:
        """Send content to user"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            environ["SMTP_HOST"], self.port, context=context
        ) as server:
            server.login(environ["SMTP_EMAIL"], self.password)
            server.sendmail(environ["SMTP_EMAIL"], user.email, content)
