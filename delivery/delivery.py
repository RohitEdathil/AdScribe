from abc import ABC, abstractmethod
from ..models import User


class Delivery(ABC):
    @abstractmethod
    def deliver(self, user: User, content: str) -> None:
        pass
