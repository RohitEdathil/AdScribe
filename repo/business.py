from abc import ABC, abstractmethod
from models.product import Product
from models.user import User
from typing import List


class BusinessRepository(ABC):
    @abstractmethod
    def get_users(self) -> List[User]:
        """Fetches all users from the repository"""
        pass

    @abstractmethod
    def get_products(self) -> List[Product]:
        """Fetches all products from the repository"""
        pass
