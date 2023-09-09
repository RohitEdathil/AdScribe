from abc import ABC, abstractmethod
from models.user import User


class Delivery(ABC):
    """Abstract class for delivery methods"""

    @abstractmethod
    def deliver(self, user: User, content: str) -> None:
        """Send content to user"""
        pass
