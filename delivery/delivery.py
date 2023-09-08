from abc import ABC, abstractmethod
from models.user import User


class Delivery(ABC):
    @abstractmethod
    def deliver(self, user: User, content: str) -> None:
        pass
